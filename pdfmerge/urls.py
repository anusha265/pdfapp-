from django.urls import path
from . import views

app_name = 'pdfmerge'

urlpatterns = [
    path('merge/', views.merge_pdf_view, name='merge_pdf'),
]
