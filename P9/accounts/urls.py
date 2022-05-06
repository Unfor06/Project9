from django.urls import include, path
from .views import signup, logout_user

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
]