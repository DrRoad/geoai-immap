'''GEE settings expressed as dicts'''

BBOX = {
    'riohacha': [-73.17020892181104, 11.560920839000062, -72.52724612099996, 10.948171764015513],
    'maicao': [-72.65839212899994, 11.534938376940019, -72.15850845943176, 11.080548632000045],
    'uribia': [-72.37971307699996, 11.747684544661437, -72.15636466747618, 11.523307245000069],

    'arauca': [-71.20643772199998,6.424234499000022,-69.72014485099999,7.104161825000062],
    'arauquita': [-71.69980876899996,6.526376968000022,-70.86773583299998,7.054700505000028], 
    'cucuta': [-72.60807671699996,7.723856582000053,-72.34649040099998,8.431575791000057], 
    'tibu': [-73.07343705199997,8.251246337000055,-72.47112479799995,9.142041082000048], 
    'soacha': [-74.30657295399999,4.382138206000036,-74.17129610699999,4.633509322000066], 

    'soledad': [-74.83911786099998,10.874457188000065,-74.71833013999998,10.945374659000038],
    'sabanalarga': [-73.07842230299997,4.65890958600005,-72.86002019499995,5.003081439000027],
    'santamaria': [-74.24179670499996,10.823943058000054,-73.56533005099999,11.34891206900005],
    'bogota': [-74.45085037099994,3.7306330990000447,-73.98612579299999,4.836827395000057],
    'barranquilla': [-74.91914036699995,10.913916096000037,-74.75583470399994,11.10537038700005],
    
    'yopal': [-72.58406014999997,4.903336589000048,-71.93890813899998,5.570461942000065],
    
    'puertocarreno': [-68.82495382199994,5.301608556000076,-67.40421439099998,6.320010965000051],
    'bucaramanga': [-73.17268342899996,7.072426422000035,-73.04434350999998,7.258320651000076],
    'inirida': [-69.41609224999996,2.362370110000029,-67.53801119699995,4.045202374000041],
    'monteria': [-76.26815760199997,8.238202150000063,-75.66964288399998,8.95248753900006],
    'fonseca': [-72.92277095999998,10.648138715000073,-72.67409870999995,11.031392905000075],
    
    'fortul' : [-72.13711557299996,6.507671884000047,-71.47137503599998,6.862336441000025],
    'fundacion' : [-74.21899133699998,10.274034250000057,-73.56065982199993,10.64480271800005],
    'malambo' : [-74.88227861299998,10.81137343000006,-74.73317731399999,10.890650812000047],
    'manaure' : [-72.90465776982178,11.418217478425655,-72.25823464154773,11.84201355422358],
    'ocana' : [-73.52976829299996,8.012779764000072,-73.24983552699996,8.428422113000067],
    'pasto' : [-77.36181940199998,0.7626372470000433,-77.03029201699997,1.3284817530000623],
    'puertosantander' : [-72.44813870750166,8.268193768578357,-72.37877552755887,8.386519193186638],
    'saravena' : [-72.09962277499994,6.745921904000056,-71.69442685499996,7.0810649060000515],
    'villadelrosario' : [-72.52267855299993,7.64295204900003,-72.44465188199996,7.902600765000045],
    'tame' : [-71.86701035838708,6.401026857098356,-71.62082292314204,6.5154961741231165],
    'yopal' : [-72.58406014999997,4.903336589000048,-71.93890813899998,5.570461942000065],
    
}



# cloud filter and if mask is applied
CLOUD_PARAMS = {
    'riohacha': {
        '2015-2016': (30, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'maicao': {
        '2015-2016': (20, True), 
        '2017-2018': (40, True), 
        '2019-2020': (40, True), 
    },
    'uribia': {
        '2015-2016': (10, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    }, 

    'arauca': {
        '2015-2016': (10, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'arauquita': {
        '2015-2016': (10, False), 
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'cucuta': {
        '2015-2016': (10, True), 
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'tibu': {
        '2015-2016': (10, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'soacha': {
        '2015-2016': (10, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },

    'bogota': {
        '2015-2016': (20, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    
    'yopal': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },

    'puertocarreno': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'bucaramanga': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'inirida': {
        '2015-2016': (20, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'monteria': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'fonseca': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },

    'fortul': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'fundacion': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'malambo': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'manaure': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'ocana': {
        '2015-2016': (10, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'pasto': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'puertosantander': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'saravena': {
        '2015-2016': (20, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'villadelrosario': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'tame': {
        '2015-2016': (20, False),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },
    'yopal': {
        '2015-2016': (40, True),
        '2017-2018': (40, True),
        '2019-2020': (40, True),
    },

}

# Get name in shapefile
admin2RefN = {
    'riohacha': 'Riohacha', 
    'maicao': 'Maicao', 
    'uribia': 'Uribia',
    
    'arauca': 'Arauca', 
    'arauquita': 'Arauquita', 
    'cucuta': 'Cucuta', 
    'tibu': 'Tibu', 
    'soacha': 'Soacha', 
    'villadelrosario': 'Villa del Rosario',
    'saravena': 'Saravena',
    
    'soledad': 'Soledad', 
    'sabanalarga': 'Sabanalarga',
    'santamarta': 'Santa Marta',
    'bogota': 'Bogota D.C.',
    'barranquilla': 'Barranquilla',
    
    'yopal': 'Yopal',
    
    'puertocarreno': 'Puerto Carreno', 
    'bucaramanga': 'Bucaramanga',
    'inirida': 'Inirida',
    'monteria': 'Monteria',
    'fonseca': 'Fonseca',
    
    'fortul': 'Fortul',
    'fundacion': 'Fundacion',
    'malambo': 'Malambo',
    'manaure': 'Manaure',
    'ocana': 'Ocana',
    'pasto': 'Pasto',
    'puertosantander': 'Puerto Santander',
    'tame2': 'Tame',
    'yopal': 'Yopal',
    
}