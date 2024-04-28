from django.urls import path
from .views import item_list, item_detail, MyItem

urlpatterns = [
    # ------ Function Based View------
    # path('', item_list),
    # path('item/<int:pk>/', item_detail),
    
    
    # ------- Class Based View----
    path('',MyItem.as_view()),
    path('item/<int:pk>/', MyItem.as_view()),
    
    
    # ------- Generic View-----
    path()
    
    
    
]
