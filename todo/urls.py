from django.contrib import admin
from django.urls import path
from app1.views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("rejalar", RejaVs)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

