from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from basicCrud.models import Item
from basicCrud.serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ViewSet):
    
    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        