from django.urls import include, path
from rest_framework import routers
from common.views import (CompanyListAPIView, CustomerListAPIView, RequestHouseMoveListAPIView, CarViewSet,
                          CompanyViewSet, CompanyCarCountViewSet, CustomerViewSet, MoveFeedbackViewSet,
                          RequestHouseMoveViewSet,)

router = routers.DefaultRouter()
router.register(r'set/car', CarViewSet)
router.register(r'set/company', CompanyViewSet)
router.register(r'set/compnay_car_count', CompanyCarCountViewSet)
router.register(r'set/customer', CustomerViewSet)
router.register(r'set/feedback', MoveFeedbackViewSet)
router.register(r'set/request', RequestHouseMoveViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company/', CompanyListAPIView.as_view()),
    path('customer/', CustomerListAPIView.as_view()),
    path('request/house/', RequestHouseMoveListAPIView.as_view()),
]
