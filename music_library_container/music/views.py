from django.http.response import Http404
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SongList(APIView):
    '''Read op on all songs in the dataset and Create op to add a new one'''

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):
    '''Read, Update, Delete operations for an individual song'''

    def get_object(self, id):
        try:
            return Song.objects.get(pk=id)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        song.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
