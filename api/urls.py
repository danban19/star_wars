from django.urls import path
from .views import start_view, character_view, collections_view


urlpatterns = [
    path('start/', start_view),
    path('characters/', character_view),
    path('collections/', collections_view)
]
