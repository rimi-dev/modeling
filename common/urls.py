from django.urls import include, path
from rest_framework import routers
from common.views import (CompanyListAPIView, CustomerListAPIView, RequestHouseMoveListAPIView)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('company/list', CompanyListAPIView.as_view()),
    path('customer/list', CustomerListAPIView.as_view()),
    path('request/house/list', RequestHouseMoveListAPIView.as_view()),
]
