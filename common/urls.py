from django.urls import include, path
from rest_framework import routers
from common.views import (CompanyListAPIView, CustomerListAPIView, RequestHouseMoveListAPIView, CarViewSet,
                          )

router = routers.DefaultRouter()
router.register(r'car', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company/', CompanyListAPIView.as_view()),
    path('customer/', CustomerListAPIView.as_view()),
    path('request/house/', RequestHouseMoveListAPIView.as_view()),
]
