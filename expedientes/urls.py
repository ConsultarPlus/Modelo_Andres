from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views
from django.views.generic import RedirectView
from django.contrib.auth import logout


from . import views
urlpatterns = [
    url(r'^$', login_required(views.Home.as_view()), name='home'),
    url(r'^home/$', login_required(views.Home.as_view()), name='home_2'),
    #url(r'^expedientes/$', login_required(views.ExpedientesList.as_view()), name='expedientes'),
    url(r'^expedientes/(?P<pk>\d+)/$', login_required(views.expediente_dsp_view), name='expediente_dsp_view'),
    url(r'^expedientes/(?P<pk>\d+)/upd/$', login_required(views.expediente_upd_view), name='expediente_upd_view'),
    url(r'^expedientes/alta/$', login_required(views.ExpedienteCreateView.as_view()), name='ExpedienteCreateView'),
    url(r'^expedientes/(?P<pk>\d+)/baja/$', login_required(views.expediente_baja_view), name='expediente_baja_view'),
    url(r'^expedientes/$', login_required(views.search), name='expedientes'),
    ]
