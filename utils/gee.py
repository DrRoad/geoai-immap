import math

import ee
ee.Authenticate()
ee.Initialize()

#+++++++++++ FUNCTIONS ++++++++++++++++++++++++++
def imports2(img) :
    s2 = img.select(['B1','B2','B3','B4','B5','B6','B7','B8','B8A','B9','B11','B12'])\
             .divide(10000).addBands(img.select('QA60'))\
             .set('solar_azimuth',img.get('MEAN_SOLAR_AZIMUTH_ANGLE'))\
             .set('solar_zenith',img.get('MEAN_SOLAR_ZENITH_ANGLE'))
    #['B1','B2','B3','B4','B6','B8A','B9','B10', 'B11','B12'],\
    #['aerosol', 'blue', 'green', 'red', 'red2','red4','h2o', 'cirrus','swir1', 'swir2'])\
    return s2

def rescale(img, thresholds):
    """
    Linear stretch of image between two threshold values.
    """
    return img.subtract(thresholds[0]).divide(thresholds[1] - thresholds[0])

def sentinelCloudScore(img):
    """
    Computes spectral indices of cloudyness and take the minimum of them.

    Each spectral index is fairly lenient because the group minimum 
    is a somewhat stringent comparison policy. side note -> this seems like a job for machine learning :)

    originally written by Matt Hancher for Landsat imagery
    adapted to Sentinel by Chris Hewig and Ian Housman
    """

    # cloud until proven otherwise
    score = ee.Image(1)

    # clouds are reasonably bright
    score = score.min(rescale(img.select(['B2']), [0.1, 0.5]))
    score = score.min(rescale(img.select(['B1']), [0.1, 0.3]))
    #score = score.min(rescale(img.select(['B1']).add(img.select(['B10'])), [0.15, 0.2]))
    score = score.min(rescale(img.select(['B4']).add(img.select(['B3'])).add(img.select('B2')), [0.2, 0.8]))

    # clouds are moist
    ndmi = img.normalizedDifference(['B8A','B11'])
    score=score.min(rescale(ndmi, [-0.1, 0.1]))

    # clouds are not snow.
    ndsi = img.normalizedDifference(['B3', 'B11'])
    score=score.min(rescale(ndsi, [0.8, 0.6])).rename(['cloudScore'])

    return img.addBands(score)

# author: Nick Clinton
def ESAcloud(img) :
    """
    European Space Agency (ESA) clouds from 'QA60', i.e. Quality Assessment band at 60m

    parsed by Nick Clinton
    """

    qa = img.select('QA60')

    # bits 10 and 11 are clouds and cirrus
    cloudBitMask = int(2**10)
    cirrusBitMask = int(2**11)

    # both flags set to zero indicates clear conditions.
    clear = qa.bitwiseAnd(cloudBitMask).eq(0).And(\
           qa.bitwiseAnd(cirrusBitMask).eq(0))

    # clouds is not clear
    cloud = clear.Not().rename(['ESA_clouds'])

    # return the masked and scaled data.
    return cloud


# Author: Gennadii Donchyts
# License: Apache 2.0
def shadowMask(img,cloudMaskType):
    """
    Finds cloud shadows in images

    Originally by Gennadii Donchyts, adapted by Ian Housman
    """

    def potentialShadow(cloudHeight):
        """
        Finds potential shadow areas from array of cloud heights

        returns an image stack (i.e. list of images) 
        """
        cloudHeight = ee.Number(cloudHeight)

        # shadow vector length
        shadowVector = zenith.tan().multiply(cloudHeight)

        # x and y components of shadow vector length
        x = azimuth.cos().multiply(shadowVector).divide(nominalScale).round()
        y = azimuth.sin().multiply(shadowVector).divide(nominalScale).round()

        # affine translation of clouds
        cloudShift = cloudMask.changeProj(cloudMask.projection(), cloudMask.projection().translate(x, y)) # could incorporate shadow stretch?

        return cloudShift

    # select a cloud mask
    cloudMask = img.select(cloudMaskType)

    # make sure it is binary (i.e. apply threshold to cloud score)
    cloudScoreThreshold = 0.5
    cloudMask = cloudMask.gt(cloudScoreThreshold)

    # solar geometry (radians)
    azimuth = ee.Number(img.get('solar_azimuth')).multiply(math.pi).divide(180.0).add(ee.Number(0.5).multiply(math.pi))
    zenith  = ee.Number(0.5).multiply(math.pi ).subtract(ee.Number(img.get('solar_zenith')).multiply(math.pi).divide(180.0))

    # find potential shadow areas based on cloud and solar geometry
    nominalScale = cloudMask.projection().nominalScale()
    cloudHeights = ee.List.sequence(500,4000,500)        
    potentialShadowStack = cloudHeights.map(potentialShadow)
    potentialShadow = ee.ImageCollection.fromImages(potentialShadowStack).max()

    # shadows are not clouds
    potentialShadow = potentialShadow.And(cloudMask.Not())

    # (modified) dark pixel detection 
    darkPixels = img.normalizedDifference(['B3', 'B12']).gt(0.25)

    # shadows are dark
    shadows = potentialShadow.And(darkPixels).rename(['shadows'])

    # might be scope for one last check here. Dark surfaces (e.g. water, basalt, etc.) cause shadow commission errors.
    # perhaps using a NDWI (e.g. B3 and nir)

    return shadows

# Run the cloud masking code
def cloud_and_shadow_mask(img) :
    s2 = imports2(img)
    s2 = sentinelCloudScore(s2)
    cloud = ESAcloud(s2)
    shadow = shadowMask(s2,'cloudScore')
    mask = cloud.Or(shadow).eq(0)

    return s2.updateMask(mask)

# Run the cloud masking code
def cloud_mask(img) :
    s2 = imports2(img)
    cloud = ESAcloud(s2)
    mask = cloud.eq(0)
    return s2.updateMask(mask)

def sen2median(BBOX, year, FILENAME):
    '''
    Downloads Sentinel Year Median Aggregate Composite for specified bounding box and year.
    For status, check https://code.earthengine.google.com/
    
    Args
        BBOX (list of 4 floats): bounding box coordinates; x,y left, top, right, bottom
    
    References
    https://github.com/samsammurphy/cloud-masking-sentinel2
    https://github.com/giswqs/qgis-earthengine-examples
    https://developers.google.com/earth-engine/python_install#syntax
        
    '''
    
    # select product
    print(f'Processing {FILENAME}')
    if year <= 2017:
        PRODUCT = 'COPERNICUS/S2' # S2 for L1C <=2017 
    else:
        PRODUCT = 'COPERNICUS/S2_SR' # and S2_SR for L2A

    print(f'using {PRODUCT}')
          
    # set date window
    date1 = f'{year}-01-01'
    date2 = f'{year}-12-31'

    # select region
    region = ee.Geometry.Rectangle(BBOX) # restrict view to bounding box

    #+++++++++++ DISPLAY IMAGE ++++++++++++++++++++++++++

    #obtain the S2 image
    S2 = (ee.ImageCollection(PRODUCT)
     .filterDate(date1, date2)
     .filterBounds(region))
    # .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10))


    # # View specific images
    # S2 = ee.ImageCollection.fromImages([
    #   ee.Image('COPERNICUS/S2/20160213T150652_20160213T150654_T19NCH'),
    #   ee.Image('COPERNICUS/S2/20160213T150654_20160213T214357_T19NCH')
    #   ])

    #call the cloud masking functions
    composite = (S2
      .map(cloud_and_shadow_mask)
      .median())

    # # [WIP] Get the following info from the nested dict
    # # id
    # # PRODUCT_ID
    # # CLOUDY_PIXEL_PERCENTAGE
    # temp = S2.getInfo()
    # # source: https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists
    # def gen_dict_extract(key, var):
    #     if hasattr(var,'iteritems'):
    #         for k, v in var.iteritems():
    #             if k == key:
    #                 yield v
    #             if isinstance(v, dict):
    #                 for result in gen_dict_extract(key, v):
    #                     yield result
    #             elif isinstance(v, list):
    #                 for d in v:
    #                     for result in gen_dict_extract(key, d):
    #                         yield result

    # Export task
    task = ee.batch.Export.image.toCloudStorage(
      image= composite.select(['B1','B2','B3','B4','B5','B6','B7','B8','B8A','B9','B11','B12']),
      description= FILENAME,
      bucket= 'immap-gee',
      maxPixels= 150000000,
      scale= 10,
      region= region,
      crs= 'EPSG:4326'
    )

    task.start()
    print('Task started')
    # task.status()