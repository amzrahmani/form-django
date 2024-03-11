from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name="home"),
    path('detail/<int:post_id>/',views.detail,name="details"),
    path('delete/<int:post_id>/',views.delete,name="delete"),
    path('create/', views.create, name="create"),

]