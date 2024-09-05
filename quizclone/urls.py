from django.urls import path
from .views import GetDBClone


urlpatterns = [
    path("getdb/", GetDBClone.as_view()),
]
