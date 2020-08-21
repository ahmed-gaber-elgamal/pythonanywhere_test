from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users$', views.UserIndex, name='users'),
    # url(r'^form$', views.user_form_view, name='form'),
    url(r'^register$', views.register, name='register')

    # path('', views.index, name='index'),
]