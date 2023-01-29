from django.urls import path
from . import views
app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('produto', views.produto, name='produto'),
    path('service', views.service, name='service'),
    path('myCalc/<str:arg>', views.myCalc, name='myCalc')
]
