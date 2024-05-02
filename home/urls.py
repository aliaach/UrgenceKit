from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index
from . import views  # Import your views module
from .views import add_to_favorites


from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
   #path('purchase/<int:id>/', views.purchase_kit, name='purchase_kit'),
    path('add_to_favorites/<int:kit_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorite_kits/', views.favorite_kits, name='favorite_kits'),
      path('chatbot/', views.chatbot_view, name='chatbot'),
   
    
    
     
]


