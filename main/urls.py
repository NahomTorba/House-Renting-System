from django.urls import path
from . import views

from django.views.i18n import set_language
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', views.index, name="index"),
path('index.html', views.index, name="index"),
path("contact.html", views.contact, name="contact"),
path("about.html", views.about, name="about"),
path("property-agent.html", views.property_agent, name="property-agent"),
path("property-list.html", views.property_list, name="property-list"),
path("property-type.html", views.property_type, name="property-type"),
path("testimonial.html", views.testimonial, name="testimonial"),
path("404.html", views.not_found, name="404"),
path("signup.html/", views.signup, name="signup"),
path("Login.html/", views.Login, name="Login"),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('set_language/', set_language, name='set_language'),
]
