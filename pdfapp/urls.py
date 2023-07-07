from django.urls import path
from pdfmerge import views

urlpatterns = [
    path('', views.merge_pdf, name='merge_pdf'),
]