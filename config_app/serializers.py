from rest_framework import serializers
from .models import Travel, Mexmonxona, Transport

from rest_framework import serializers


class TravelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    country_name = serializers.CharField(max_length=100)
    haqida = serializers.CharField()
    muddati = serializers.IntegerField()
    narxi = serializers.IntegerField()
    mexmonxona = serializers.CharField()
    transport = serializers.CharField()

    def create(self, validated_data):
        return Travel().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.haqida = validated_data.get('haqida', instance.haqida)
        instance.muddati = validated_data.get('muddati', instance.muddati)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.mexmonxona = validated_data.get('mexmonxona', instance.mexmonxona)
        instance.transport = validated_data.get('transport', instance.transport)
        instance.save()
        return instance

class MexmonxonaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    yulduzlar_soni = serializers.IntegerField()
    narxi = serializers.IntegerField()

    def create(self, validated_data):
        return Mexmonxona().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.yulduzlar_soni = validated_data.get('yulduzlar_soni', instance.yulduzlar_soni)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.save()
        return instance


class TransportSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    narxi = serializers.IntegerField()

    def create(self, validated_data):
        return Transport().objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.save()
        return instance
    