from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView
from .views import CustomPasswordResetConfirmView


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


path('view_request/<int:property_id>/', views.view_requests, name='view_requests'),
path('update_requests/<int:request_id>/', views.update_requests, name='update_requests'),
path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),
path('user_request/', views.user_requests, name='user_requests'),
path('send_request/<int:property_id>/', views.send_request, name='send_request'),

#password reseting default views
path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name="reset_password_form.html"), name="password_reset_confirm"),
path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done.html"), name="password_reset_complete"),
]
