import json

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


class ProductDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            product = Product.objects.get(pk=pk)
            product_serializer = ProductSerializer(product, many=False)
            message = product_serializer.data
        except:
            return Response({"error": "Object does not exists"})

        product_media = ProductMedia.objects.filter(product_id=product.id).all()
        product_media_serializer = ProductMediaSerializer(product_media, many=True)
        product_dict = json.loads(product_serializer.data)
        product_media_dict = json.loads(product_media_serializer.data)
        print(product_dict)
        print(product_media_dict)

        # try:
        #     product_media = ProductMedia.objects.filter(product_id=product.id).all()
        #     product_media_serializer = ProductMediaSerializer(product_media, many=True)
        #     message.update(product_media_serializer.data)
        # except:
        #     pass

        return Response(message)

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
