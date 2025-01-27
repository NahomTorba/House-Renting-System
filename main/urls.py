from django.urls import path
from . import views

from django.views.i18n import set_languagev


urlpatterns = [
path('', views.index, name="index"),
path('index.html', views.index, name="index"),
path("contact.html", views.contact, name="contact"),
path("about.html", views.about, name="about"),
path("property-agent.html", views.property_agent, name="property-agent"),
path("property-list.html", views.property_list, name="property-list"),
path("property-type.html", views.property_type, name="property-type"),
path("testimonial.html", views.testimonial, name="testimonial"),

path('set_language/', views.i18n.set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    # Your existing i18n URL patterns
)
