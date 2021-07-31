from django.urls import path
from . import views

app_name = 'sisapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('personalinfo/', views.personalinfo, name='personalinfo'),
    path('publishedres/', views.publishedres, name='publishedres'),
    path('personalacc/', views.personalacc, name='personalacc'),
    path('success/', views.success, name='success'),
    path('payments/', views.payments, name='payments'),
    path('message/', views.message, name='message'),
    path('upload_results/', views.uploadresults, name='uploadresults'),
    path('stdterm/', views.stdterm, name='stdterm'),
    path('saveresults/', views.saveresults, name='saveresults'),
    path('promote/', views.promote, name='promote'),
    path('savepayments/', views.savepayments, name='savepayments'),
]
