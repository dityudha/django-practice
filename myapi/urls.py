from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarsViewSet)
router.register(r'bike', views.BikeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# from django.conf.urls import url
# from django.urls import path, include
# from myapi.views import CarsViewSet
# from myapi.views import BikeViewSet
# from . import views


# urlpatterns = [
#     path('cars', CarsViewSet.as_view()),
#     path('bike', BikeViewSet.as_view()),
#     ]