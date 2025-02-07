from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from geojson import Feature, Point, FeatureCollection, GeometryCollection
from django.template import loader


from crt_ast.models import Asset, Point, AssetType, polygonn
from django.core.serializers import serialize

from geo.czmledit import czml
from PIL import ImageColor, Image
from geo.coordConvert import geodetic_to_geocentric
from Asset_Life_Cycle.models import LifeCyclePhase
from Task.models import Task
#import random

def czmlPoint(request):

    doc1 = czml.CZML()

    packet1 = czml.CZMLPacket(id='document',name="billboards",version='1.0')
    doc1.packets.append(packet1)

    #billboard
    for i in Point.objects.all():

        packet2 = czml.CZMLPacket(id='bb_'+ "2021" + str(100 + i.id), name=i.name, status=i.lc_phase.name)

        descri = czml.Description()

        for j in Task.objects.all():
            descri.string = "<b>Type: </b> " + i.type.name + "<br/>" + "<b>Description: </b> " + i.description + " <a href='http://geomatik.hacettepe.edu.tr/' target='_blank'>(Web Sitesi)</a>" + "<br/>" + "<b>Status: </b> " + i.lc_phase.name + "<br/>" + "<b>Task: </b> " +  str(j.description)


        packet2.description = descri

        bb = czml.Billboard(scale=i.markersize, show=True)

        a = (i.symbol).split("/")
        a = a[-1]


        bb.image ="/static/Cesium/Build/Cesium/Assets/Textures/maki/" + a ,
        bb.heightReference = "CLAMP_TO_GROUND"
        bb.clampToGround = True

        rgb = ImageColor.getcolor(i.markercolor, "RGB")
        L1=list(rgb)
        if i.lc_phase.name == "Bakımda":
            L1.append(175)
        else:
            L1.append(255)
        
        rgb=tuple(L1)

        bb.color = {'rgba': rgb} #i.markercolor

        packet2.billboard = bb

        poz = czml.Position()
        WGS84 = 6378137, 298.257223563
        poz.cartesian = geodetic_to_geocentric(WGS84, i.lat, i.lon, i.height)

        packet2.position = poz

        
        rgb2 = ImageColor.getcolor(i.lc_phase.color, "RGBA")

        lab = czml.Label()
        lab.show = True
        #lab.fillColor = {'rgba': rgb2}
        lab.text = i.lc_phase.name
        lab.heightReference = "CLAMP_TO_GROUND"
        lab.clampToGround = True
        lab.pixelOffset = {"cartesian2" : [20,-35] }
        lab.horizontalOrigin = "LEFT"
        lab.showBackground = True
        lab.backgroundColor = {'rgba': rgb2}

        packet2.label = lab

        doc1.packets.append(packet2)

        #photo kısmını kaydetmek için
        #img = i.photo
        #img.save('../static/Cesium/Build/Cesium/Assets/Textures/maki/' + str(i.id) +".png" , 'PNG')

    myczml= doc1.dumps()

    return HttpResponse(str(myczml))

    #return HttpResponse('[ { "id": "document", "name": "CZML Points", "version": "1.0", }, '+ str(points) + "]")

def czmlPolygon():
    doc1 = czml.CZML()

    packet1 = czml.CZMLPacket(id='document',name="billboards",version='1.0')
    doc2.packets.append(packet1)

    for i in polygonn.objects.all():

        packet2 = czml.CZMLPacket(id='po_'+ "2021" + str(100 + i.id), name=i.name)

        descri = czml.Description()


        descri.string = i.description

        packet2.description = descri

        po = czml.Polygon(show=True)

        po.heightReference = "CLAMP_TO_GROUND"
        po.clampToGround = True

        rgb = ImageColor.getcolor(i.markercolor, "RGB")
        L1=list(rgb)
        if i.lc_phase.name == "Bakımda":
            L1.append(175)
        else:
            L1.append(180)
        
        rgb=tuple(L1)

        mater = czml.Material(solidColor= rgb) 
        po.material = mater

        poz = czml.Positions()
        WGS84 = 6378137, 298.257223563
        poz.cartesian = geodetic_to_geocentric(WGS84, i.lat, i.lon, i.height)
        po.positions = poz

        packet2.polygon = po

        doc1.packets.append(packet2)


    myczml= doc1.dumps()

    return HttpResponse(str(myczml))

    


def cesiumAsset(request):
    geojs = serialize('geojson', Asset.objects.all(),
              geometry_field='geom',
              fields=('name', 'description', 'markercolor', 'markersymbol', 'markersize','active'))

    #results = json.loads(geojs)

    return HttpResponse(str(geojs))


"""
def s_cesiumAsset(request):
    
    features = []
    
    
    for i in Asset.objects.all():
        f = Feature(geometry=Point((i.lon, i.lat, i.alti)))
        f["id"]=i.id
        f['name']=i.name
        f['properties']["title"]= i.name
        f['properties']["markersymbol"]= i.markersymbol
        f['properties']["markercolor"]= i.markercolor
        
        features.append(f)
        
    feature_collection = FeatureCollection(features)
    
    return HttpResponse(str(feature_collection))

"""

