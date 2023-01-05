from django.urls import path
from .views import start_view, character_view, collections_view, single_collection_view


urlpatterns = [
    path('start/', start_view),
    path('characters/', character_view),
    path('collections/', collections_view),
    path('collection/<name>/', single_collection_view, name='name')
]
