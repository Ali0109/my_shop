from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from product.serializers import *


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Product.objects.get(pk=pk)

        except:
            return Response({"error": "Object does not exist"})

        instance.delete()
        return Response({"message": "Not found"})


@api_view(["PUT"])
def ProductRestoreAPIView(request, pk):
    try:
        product = Product.deleted_objects.get(pk=pk)
    except:
        return Response({"error": "Deleted object not found"})
    product.restore()
    serializer = ProductSerializer(product, many=False)
    message = {
        "message": "Data was restored",
        "data": serializer.data,
    }
    return Response(message, status=status.HTTP_200_OK)
