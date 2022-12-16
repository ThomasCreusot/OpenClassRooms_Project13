from django.urls import path

# model from documentation : https://docs.djangoproject.com/fr/4.1/topics/http/urls/#url-namespaces
# from . import views

# app_name = 'polls'
# urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
#    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#    ...
# ]

from profiles.views import index as profiles_index
from profiles.views import profile

app_name = 'profiles'
urlpatterns = [
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
