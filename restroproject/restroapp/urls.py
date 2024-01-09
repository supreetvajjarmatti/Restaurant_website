from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('about.html',views.about,name='about'),
    path('booking.html',views.booking,name='booking'),
    path('contact.html',views.contact,name='contact'),
    path('menu.html',views.menu,name='menu'),
    path('service.html',views.service,name='service'),
    path('table_booking.html',views.table_booking,name='table_booking'),
    path('team.html',views.team,name='team'),
    path('terms&condition.html',views.terms,name='terms'),
    path('testimonial.html',views.testimonial,name='testimonial'),


]