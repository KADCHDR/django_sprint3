from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.main_feed, name='main_feed'),
    path('posts/<int:entry_id>/', views.entry_view, name='entry_view'),
    path('category/<slug:cat_slug>/', views.category_view, name='category_view'),
]
