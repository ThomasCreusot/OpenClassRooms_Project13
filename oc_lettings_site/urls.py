from django.contrib import admin
from django.urls import path

from . import views

# version before namespaces
#from lettings.views import index as lettings_index
#from lettings.views import letting
#from profiles.views import index as profiles_index
#from profiles.views import profile

# version with namespaces
from django.urls import include


urlpatterns = [
    path('', views.index, name='index'),

    # initial version
    # path('lettings/', views.lettings_index, name='lettings_index'),
    # version before namespaces
    # path('lettings/', lettings_index, name='lettings_index'),

    # initial version
    # path('lettings/<int:letting_id>/', views.letting, name='letting'),
    # version before namespaces
    # path('lettings/<int:letting_id>/', letting, name='letting'),

    # initial version
    # path('profiles/', views.profiles_index, name='profiles_index'),
    # version before namespaces
    # path('profiles/', profiles_index, name='profiles_index'),

    # initial version
    # path('profiles/<str:username>/', views.profile, name='profile'),
    # version before namespaces
    # path('profiles/<str:username>/', profile, name='profile'),

    path('admin/', admin.site.urls),

    # version with namespaces
    path('author-lettings/', include('lettings.urls', namespace='author-lettings')),
    path('author-profiles/', include('profiles.urls', namespace='author-profiles')),
]
