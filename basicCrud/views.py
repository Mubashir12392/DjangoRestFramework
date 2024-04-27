from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Item
from .serializers import ItemSerializer

# Create your views here.

# We are using simple Function based view for Django Rest Framework
# Using @api_view because we want to be able to POST to this view from clients that won't have a CSRF token

# -----CRUD (Retrieve, Create)-----

@api_view(['GET','POST'])
def item_list(request):
    
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
    
    
# ----CRUD (Update , Delete)

@api_view(['GET','PUT','DELETE'])
def item_detail(request, pk):
    
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)