<<<<<<< HEAD
from django.urls import path, include

from .views import(
	home, servicos,planos, sobre, contato
) 

urlpatterns = [
	path('', home, name='website_home'),
    path('servicos', servicos, name='website_servicos'),
    path('contato', contato, name='website_contato'),
    path('planos', planos, name='website_planos'),
    path('sobre', sobre, name='website_sobre'),

]
=======
from django.conf.urls import url, include
from django.urls import path
from .views import home, contato, servicos

urlpatterns = [
    url(r'^$', home, name='website_home'),
    url(r'^contato$', contato, name='website_contato'),
    path('servicos', servicos, name='website_servicos'),
]
>>>>>>> 8aaa8fa7274a57f1c5dd7c0e8ddcdfdc4e12fc57
