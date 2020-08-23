from django.db.models import Func, F, Value, CharField
from django.db.models.functions import Cast
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from common.models import (Company, Customer, RequestHouseMove)
from common.serializers import (CompanySerializer)


class CompanyListAPIView(APIView):
    def get(self, request):
        queryset = Company.objects.annotate(
            tel_regex=Cast(
                Func(
                    F('tel'),
                    Value(r'(02|\d{2,3})(\d{4})(\d{1})(\d{2})(\d{1}$)'),
                    Value(r'\1-\2-\3**\5'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
            address_regex=Cast(
                Func(
                    F('address'),
                    Value(r'^([가-힣]{2,}) ([가-힣]{3,}) ([가-힣]{2,}동|읍|면) (.*)'),
                    Value(r'\1 \2 \3'),
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


class CustomerListAPIView(APIView):
    def get(self, request):
        queryset = Customer.objects.annotate(
            tel_regex=Cast(
                Func(
                    F('tel'),
                    Value(r'(02|\d{2,3})(\d{4})(\d{1})(\d{2})(\d{1}$)'),
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


class RequestHouseMoveListAPIView(APIView):
    def get(self, request):
        response = {}
        queryset = RequestHouseMove.objects.annotate(
            tel_regex=Cast(
                Func(
                    F('customer__tel'),
                    Value(r'(02|\d{2,3})(\d{4})(\d{1})(\d{2})(\d{1}$)'),
                    Value(r'\1-\2-\3**\5'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
            start_address_regex=Cast(
                Func(
                    F('starting_address'),
                    Value(r'^([가-힣]{2,}) ([가-힣]{3,}) ([가-힣]{2,}동|읍|면) (.*)'),
                    Value(r'\1 \2 \3'),
                    Value('g'),
                    function='regexp_replace'),
                CharField()
            ),
            end_address_regex=Cast(
                Func(
                    F('destination_address'),
                    Value(r'^([가-힣]{2,}) ([가-힣]{3,}) ([가-힣]{2,}동|읍|면) (.*)'),
                    Value(r'\1 \2 \3'),
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