from django.conf.urls import url
from loginApp import views


urlpatterns = [
    url(r'^$', views.new_user, name='register'),
    url(r'^$', views.user_login, name='login'),
]
