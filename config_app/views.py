from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Travel, Transport, Mexmonxona
from .serializers import TravelSerializer, MexmonxonaSerializer, TransportSerializer



class TravelDetailView(APIView):
    def get(self, request: Request, pk = None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except:
                return Response({"message":"Bunday sayohat turi yo'q"})
        travel = Travel.objects.all()
        return Response({'travel':TravelSerializer(travel, many=True).data})
    
    def post(self, request:Request):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        travel = serializer.save()
        return Response(TravelSerializer(travel).data)
    
    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method PUT not allowed"})
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(instance=travel, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_travel = serializer.save()
            return Response(TravelSerializer(updated_travel).data)
        except:
            return Response({"message":"Bunday sayohat turi yo'q"})
    
    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"})
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({"message":"Success"})
        except:
            return Response({"message":"Bunday sayohat turi yo'q"})
    

class TransportView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if not pk:
            transport = Transport.objects.all()
            return Response({'transport':TransportSerializer(transport, many=True).data})
        try:
            transport = Transport.objects.get(pk=pk)
            serializer = TransportSerializer(transport)
            return Response(serializer.data)
        except Transport.DoesNotExist:
            return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request:Request):
        serializer = TransportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transport = serializer.save()
        return Response(TransportSerializer(transport).data)
        
    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method PUT not allowed"})
        try:
            transport = Transport.objects.get(pk=pk)
            serializer = TransportSerializer(instance=transport, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_transport = serializer.save()
            return Response(TravelSerializer(updated_transport).data)
        except:
            return Response({"message":"Bunday transport turi yo'q"})
        

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"})
        try:
            transport = Transport.objects.get(pk=pk)
            transport.delete()
            return Response({"message":"Success"})
        except:
            return Response({"message":"Bunday transport turi yo'q"})



class MexmonxonaView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if not pk:
            mexmonxona = Mexmonxona.objects.all()
            return Response({'mexmonxona':MexmonxonaSerializer(mexmonxona, many=True).data})
        try:
            mexmonxona = Mexmonxona.objects.get(pk=pk)
            serializer = MexmonxonaSerializer(mexmonxona)
            return Response(serializer.data)
        except Mexmonxona.DoesNotExist:
            return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request:Request):
        serializer = MexmonxonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mexmonxona = serializer.save()
        return Response(TravelSerializer(mexmonxona).data)
        

    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method PUT not allowed"})
        try:
            mexmonxona = Mexmonxona.objects.get(pk=pk)
            serializer = MexmonxonaSerializer(instance=mexmonxona, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_mexmonxona = serializer.save()
            return Response(TravelSerializer(updated_mexmonxona).data)
        except:
            return Response({"message":"Bunday mexmonxona turi yo'q"})
        

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"})
        try:
            mexmonxona = Mexmonxona.objects.get(pk=pk)
            mexmonxona.delete()
            return Response({"message":"Success"})
        except:
            return Response({"message":"Bunday mexmonxona turi yo'q"})