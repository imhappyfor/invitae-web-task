"""webtask URL Configuration"""
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('genome/', include('genome.urls', namespace='genome')),
    # path('/genome_render/', include('genome_render.urls', namespace='genome_render')),
    path('admin/', admin.site.urls),
]
