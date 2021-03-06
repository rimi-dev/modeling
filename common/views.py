from django.db.models import Func, F, Value, CharField
from django.db.models.functions import Cast
from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from common.models import (Company, Customer, RequestHouseMove, Car, CompanyCarCount, MoveFeedback)
from common.serializers import (CarSerializer, CompanySerializer, CompanyCarCountSerializer, CustomerSerializer,
                                RequestHouseMoveSerializer, MoveFeedbackSerializer)


class CompanyAPIView(APIView):
    def get(self, request):
        queryset = Company.objects.annotate(
            tel_regex=Cast(
                Func(
                    F('tel'),
                    Value(r'(02|\d{2,3})?(\d{3,})(\d{1})(\d{2})(\d{1}$)'),
                    Value(r'\1-\2-\3**\5'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
            address_regex=Cast(
                Func(
                    F('address'),
                    Value(r'(.*[시|군|구] [가-힣]{1,}[동|읍|리]) .*'),
                    Value(r'\1'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
        ).values(
            업체명=F('name'),
            연락처=F('tel_regex'),
            주소정보=F('address_regex'),
            매칭가능여부=F('is_matching'),
        )
        return Response(queryset, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CustomerAPIView(APIView):
    def get(self, request):
        queryset = Customer.objects.annotate(
            tel_regex=Cast(
                Func(
                    F('tel'),
                    Value(r'(02|\d{2,3})(\d{3,})(\d{1})(\d{2})(\d{1}$)'),
                    Value(r'\1-\2-\3**\5'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
        ).values(
            이름=F('name'),
            연락처=F('tel_regex'),
        )
        return Response(queryset, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RequestHouseMoveAPIView(APIView):
    def get(self, request):
        response = {}
        queryset = RequestHouseMove.objects.annotate(
            tel_regex=Cast(
                Func(
                    F('customer__tel'),
                    Value(r'(02|\d{2,3})(\d{3,})(\d{1})(\d{2})(\d{1}$)'),
                    Value(r'\1-\2-\3**\5'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
            start_address_regex=Cast(
                Func(
                    F('starting_address'),
                    Value(r'(.*[시|군|구] [가-힣]{1,}[동|읍|리]) .*'),
                    Value(r'\1'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
            end_address_regex=Cast(
                Func(
                    F('destination_address'),
                    Value(r'(.*[시|군|구] [가-힣]{1,}[동|읍|리]) .*'),
                    Value(r'\1'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
        ).values(
            이름=F('customer__name'),
            연락처=F('tel_regex'),
            출발지=F('start_address_regex'),
            도착지=F('end_address_regex'),
            이사일자=F('move_date'),
            보관이사여부=F('is_storage'),
        )
        response['total_data_count'] = queryset.count()
        response['result'] = queryset
        print(response)
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RequestHouseMoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CompanyCarCountViewSet(ModelViewSet):
    queryset = CompanyCarCount.objects.all()
    serializer_class = CompanyCarCountSerializer


class MoveFeedbackViewSet(ModelViewSet):
    queryset = MoveFeedback.objects.all()
    serializer_class = MoveFeedbackSerializer
