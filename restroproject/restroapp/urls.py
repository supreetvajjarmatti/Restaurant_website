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
    path('team.html',views.team,name='team'),
    path('terms&condition.html',views.terms,name='terms'),
    path('testimonial.html',views.testimonial,name='testimonial'),
    path('success_test.html',views.success,name='success'),
    path('table_booking', views.reservation_view, name='reservation_view'),
    path('succes_page.html',views.success_page,name='success_page'),
    path('booking.html', views.reservation_view, name='reservation_view'),



]