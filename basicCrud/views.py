from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status

from .models import MyItem
from .serializers import ItemSerializer

# Create your views here.

# __________________________________________ Function Based View_______________________


# Using @api_view because we want to be able to POST to this view from clients that won't have a CSRF token

# -----CRUD (Retrieve, Create)-----


@api_view(["GET", "POST"])
def item_list(request):

    if request.method == "GET":
        items = MyItem.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----CRUD (Update , Delete)


@api_view(["GET", "PUT", "DELETE"])
def item_detail(request, pk):

    try:
        item = MyItem.objects.get(pk=pk)
    except MyItem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ________________________________________________ Class Based View _____________________________________


class Item(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            item = MyItem.objects.get(id=id)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        else:
            items = MyItem.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        try:
            item = MyItem.objects.get(pk=pk)
        except MyItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = MyItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# _____________________________________ Generic Views_________________________________


# ----CRUD (Read--Manyitems)
class ListItem(ListAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


# ----CRUD (Read--Singleitem)
class ReadItem(RetrieveAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


# ----CRUD (Create)
class CreateItem(CreateAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


# ----CRUD (Update)
class UpdateItem(UpdateAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


# ----CRUD (Delete)
class DeleteItem(DestroyAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


class ReadCreateItem(ListCreateAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


class ReadSingleUpdateItem(RetrieveUpdateAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


class ReadSingleDeleteItem(RetrieveDestroyAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer


class ReadUpdateDeleteItem(RetrieveUpdateDestroyAPIView):
    queryset = MyItem.objects.all()
    serializer_class = ItemSerializer
