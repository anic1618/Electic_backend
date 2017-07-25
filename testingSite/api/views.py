from django.core import serializers
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.renderers import JSONRenderer

from ..models import Readings, Details, PostData
from .serializers import ReadingsSerializer, PostDataSerializer
from django.contrib.auth.models import User


class AllReadingsListView(generics.ListAPIView):
    queryset = Readings.objects.all()
    serializer_class = ReadingsSerializer

'''
todo:use current time to extract last 24 hours readings
     authentication & only post request
'''
def CurrentReading(request):
    # user = Details.objects.filter(user_id=request.user.id)
    user = User.objects.get(id=4)
    details = Details.objects.filter(user_id=user.id)
    ##for now it is getting top 24 hour rating of meter,which can be removed latter

    data = Readings.objects.filter(meter_id=details[0].meter_id).only('timestamp', 'readings')[:24]
    # max_r = data.aggregate(Max('readings')).get('readings__max', 0.00)
    # min_r = data.aggregate(Min('readings')).get('readings__min', 0.00)
    # avg_r = data.aggregate(Avg('readings')).get('readings__avg', 0.00)

    # temp = ReadingsSerializer(Readings.objects.filter(meter_id=details[0].meter_id))
    temp = ReadingsSerializer(data, many=True)
    temp = str(JSONRenderer().render(temp.data))
    temp = temp[2:len(temp) - 1]  # to remove b & \'
    # temp.replace("\"", "'");
    pst_data = PostData(user, temp)
    pst_data.meter_id = details[0].meter_id
    post_data = PostDataSerializer(pst_data)

    response = HttpResponse("{ \"result\" :" + str(post_data.data)
                            + "}",
                            content_type="application/json")

    return response



def getSummary(request):
    # user = Details.objects.filter(user_id=request.user.id)
    user = User.objects.get(id=4)
    meter_id = Details.objects.filter(user_id=user.id)[0].meter_id


