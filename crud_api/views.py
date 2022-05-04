from rest_framework import generics
from crud.models import Client, Product, Bills_Product, Bill
from .serializers import ClientSerializer,ProductSerializer,Bills_ProductSerializer,BillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_overview(request):
	api_urls = {
		'Clients':'http://127.0.0.1:8000/api/client/',
		'Bills':'http://127.0.0.1:8000/api/bill/',
        'Products':'http://127.0.0.1:8000/api/product/',
        'Bill-Products':'http://127.0.0.1:8000/api/bill-products/',

		}

	return Response(api_urls)
#Client
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#Bills
class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDetail(generics.RetrieveDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

#Bills_Product
class Bills_ProductList(generics.ListCreateAPIView):
    queryset = Bills_Product.objects.all()
    serializer_class = Bills_ProductSerializer


class Bills_ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Bills_Product.objects.all()
    serializer_class = Bills_ProductSerializer