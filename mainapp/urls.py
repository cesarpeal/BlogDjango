from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_items, name="show_items"),
	path('index/', views.show_items, name="index"),
	path('items_by_category/<str:category>', views.show_items, name="items_by_category"),
	path('registro/', views.register_page, name="register"),
	path('login/', views.login, name="login"),
	path('logout/', views.logoutUser, name="logout"),
]