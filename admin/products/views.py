from rest_framework import viewsets, status
from rest_framework.Response import Response
from rest_framework.views import APIView


from .models import Product, User
from .producer import publish
from .serializer import ProductSerializer
import random


class ProductViewSet(viewsets.Viewset):
    def list(self, request):
        product = Product.Objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data)

    def creeate(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(srializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=none): #/api/products/<str:id>
        product = Product.Objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=none): #/api/products/<str:id>
        product = Product.Objects.get(id=pk)
        serializer = ProductSerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=none): #/api/products/<str:id>
        product = Product.Objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.Objects.all()
        user = rendom.choice(users)
        return Response({
            'id': user.id
        })