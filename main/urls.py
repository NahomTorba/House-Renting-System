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
path('property-list/edit/<int:property_id>/', views.edit_property, name='edit_property'),
path('property-list/delete/<int:property_id>/', views.delete_property, name='delete_property'),
path("testimonial/", views.testimonial, name="testimonial"),
path("404/", views.not_found, name="404"),
path("signup/", views.signup, name="signup"),
path('login/', views.Login, name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('chapa/', views.chapa, name='chapa'),
path('chapa/<int:property_id>/', views.chapa, name='chapa'),
path('set_language/', set_language, name='set_language'),

path('view_request/<int:property_id>/', views.view_requests, name='view_requests'),
path('update_requests/<int:request_id>/', views.update_requests, name='update_requests'),
path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),
path('user_request/', views.user_requests, name='user_requests'),
path('send_request/<int:property_id>/', views.send_request, name='send_request'),
]
