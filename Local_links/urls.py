from django.urls import path, include
from rest_framework import routers
from .views import FarmerViewSet

router = routers.DefaultRouters()

router.register(r'farmers',FarmerViewSet)

urlpatterns = [
    path('api/',include(router.urls))

]