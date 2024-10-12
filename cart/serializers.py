from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.IntegerField(default=0)
    oprice = serializers.IntegerField(default=0)
    description = serializers.CharField(max_length=200)
    Shop = serializers.CharField(max_length=200, default='')
    mobile = serializers.IntegerField(default=0)



