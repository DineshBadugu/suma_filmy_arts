from django.urls import path
from FilmyApp import views
urlpatterns = [
    path('', views.about,name='home'),
    path('', views.about,name='about'),
    path('', views.portfolio,name='portfolio'),
    path('', views.news_events,name='news_events'),
    path('', views.contact,name='contact'),
]
