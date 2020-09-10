from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'/register/',views.register), #1
    url(r'/verify_account/',views.verify), #2
    url(r'/set_password/[0-9]+/',views.set_password), #3
    url(r'/set_password_done/',views.set_password_done),
    url(r'/login/',views.login),
    url(r'/forgot/',views.forgot), #1
    url(r'/reset_link_sent/',views.reset_link_sent), #2
    url(r'/reset/[0-9]+/',views.reset), #3
    url(r'/reset_done/',views.reset_done), #4
    url(r'/me/',views.me),
]