from django.urls import path
from src.api.views import character


urlpatterns = [
    path('characters/', character)
]
