from django.urls import path
from . import views as genome_views

app_name = 'genome'
urlpatterns = [
    path('upload', genome_views.upload, name='upload'),
    path('view', genome_views.view, name='view'),
    path('view/data' ,genome_views.viewData)
]
