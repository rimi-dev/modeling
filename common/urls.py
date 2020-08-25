from django.urls import include, path
from rest_framework import routers
from common.views import (CompanyAPIView, CustomerAPIView, RequestHouseMoveAPIView, CarViewSet,
                          CompanyCarCountViewSet, MoveFeedbackViewSet, )

router = routers.DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'car_count', CompanyCarCountViewSet)
router.register(r'feedback', MoveFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company/', CompanyAPIView.as_view()),
    path('customer/', CustomerAPIView.as_view()),
    path('request/house/', RequestHouseMoveAPIView.as_view()),
]
