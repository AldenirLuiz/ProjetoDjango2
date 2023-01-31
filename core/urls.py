from django.urls import path
from . import views
app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('produto', views.produto, name='produto'),
    path('service', views.service, name='service'),
    path('charts', views.charts, name='charts'),
    path('estoque', views.estoque, name='estoque')
]
