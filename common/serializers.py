from rest_framework import serializers
from common.models import (Company, Customer, RequestHouseMove, Car, CompanyCarCount, MoveFeedback)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCarCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCarCount
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class MoveFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveFeedback
        fields = '__all__'


class RequestHouseMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestHouseMove
        fields = '__all__'
