from django.urls import path

from moto_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('tables', views.tables, name="tables"),
    path('register/', views.register_view, name='register')
]
