from django.urls import path, include

# views
from api import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>', views.movie)
]
