from django.conf.urls import url
from AppTwo import views


urlpatterns = [
    # url("", views.help_site, name='help_site'),
    url("user/", views.user_page, name="user_page"),

    url("help/", views.help_site, name="help_site"),

    url("home/", views.index, name="index"),

    # url("registration/", views.registration, name="registration"),

]