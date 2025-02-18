from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.views.i18n import set_language

urlpatterns = [
path('', views.index, name="index"),
path('index/', views.index, name="index"),
path("contact/", views.contact, name="contact"),
path("about/", views.about, name="about"),
path("property-agent/", views.property_agent, name="property-agent"),
path("property-list/", views.property_list, name="property-list"),
path("property-type/", views.property_type, name="property-type"),
path("add_property/", views.add_property, name="add_property"),
path("testimonial/", views.testimonial, name="testimonial"),
path("404/", views.not_found, name="404"),
path("signup/", views.signup, name="signup"),
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('set_language/', set_language, name='set_language'),
]
