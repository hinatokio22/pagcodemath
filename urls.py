from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^matrices/', views.tipomatrices, name ="tipomatrices"),
    url(r'^matricesdoc/', views.tipomatricesdoc, name ="tipomatricesdoc"),
    url(r'^ejemplo', views.ejemploPagina, name ="ejemplo"),
    url(r'^conversorNumerico/', views.conversorNumerico, name ="conversorNumerico"),
    url(r'^Ieeetd/', views.Ieeetd, name="Ieeetd"),
    url(r'^Ieeesc/', views.Ieeesc, name="Ieeesc"),
    url(r'^biseccion/', views.biseccion, name="biseccion"),
    url(r'^reglaFalsa/', views.reglaFalsa, name="reglaFalsa"),
    url(r'^secante/', views.secante, name="secante"),
    url(r'^newtonRaphson/', views.newtonRaphson, name="newtonRaphson"),
    url(r'^raicesPolinomio/', views.raicesPolinomio, name="raicesPolinomio"),
    url(r'^evaluador/', views.evaluadorf, name="evaluadorf"),
    url(r'^derivacion/', views.derivacion, name="derivacion"),
    url(r'^rectangulos/', views.rectangulos, name="rectangulos"),
    url(r'^trapecios/', views.trapecios, name="trapecios"),
    url(r'^simpson13/', views.simpson13, name="simpson13"),
    url(r'^simpson38/', views.simpson38, name="simpson38"),
    url(r'^montecarlo/', views.montecarlo, name="montecarlo"),
    url(r'', views.index, name="index"),
]
