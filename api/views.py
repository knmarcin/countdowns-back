from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.models import Countdown
from api.serializers import CountdownsSerializer

class CountdownsViewSet(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Countdown.objects.all()
        serializer = CountdownsSerializer(queryset, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request, *args, **kwargs):
        serializer = CountdownsSerializer(data=request.data, many=False)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            date = serializer.validated_data['date']
            new_object = Countdown.objects.create(title=title,
                                                  date=date)
            new_object.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountdownDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = get_object_or_404(Countdown, pk=pk)
        serializer = CountdownsSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk, *args, **kwargs):
        serializer = CountdownsSerializer(data=request.data, many=False)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            date = serializer.validated_data['date']
            new_object = Countdown.objects.create(title=title,
                                                  date=date)
            new_object.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            object = Countdown.objects.get(id=pk)
        except Countdown.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        object.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        object = Countdown.objects.get(id=pk)
        serializer = CountdownsSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
