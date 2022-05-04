from rest_framework import serializers
from crud.models import Client,Bill,Bills_Product,Product


class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bill
		fields = '__all__'

class Bills_ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bills_Product
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'