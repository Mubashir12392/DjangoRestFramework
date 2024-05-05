from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
)

from basicCrud.models import MyItem
from basicCrud.serializers import ItemSerializer


@api_view(["GET"])
def testing_api(request):
    query_param = request.query_params.get("id")
    try:
        item_obj = MyItem.objects.get(id=query_param)
    except MyItem.DoesNotExist:
        return Response(
            {"message": f'Item "{query_param}" not found'},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = ItemSerializer(instance=item_obj)
    if serializer.data:
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def post_testing_api(request):
    data = request.data
    try:
        obj = MyItem.objects.create(**data)
        serializer = ItemSerializer(instance=obj)
        if serializer.data:
            return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_testing_api(request):
    data = request.data
    try:
        serializer = ItemSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_testing_api(request):
    query_param = int(request.query_params.get("id"))
    obj = MyItem.objects.get(id=query_param)
    obj.delete()
    return Response({"message": "Record is deleted successfully"})
