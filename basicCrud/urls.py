from django.urls import path
from .views import item_list, item_detail, MyItem,ListItem,ReadItem,CreateItem,UpdateItem,DeleteItem,ReadCreateItem, ReadSingleUpdateItem, ReadSingleDeleteItem, ReadUpdateDeleteItem


urlpatterns = [
    # ------ Function Based View------
    # path('', item_list),
    # path('item/<int:pk>/', item_detail),
    
    
    # ------- Class Based View----
    # path('',MyItem.as_view()),
    # path('item/<int:pk>/', MyItem.as_view()),
    
    
    # ------- Generic View-----
    path('',ListItem.as_view()),
    path('item/<int:pk>/',ReadItem.as_view()),
    path('createitem/',CreateItem.as_view()),
    path('updateitem/<int:pk>/',UpdateItem.as_view()),
    path('deleteitem/<int:pk>/',DeleteItem.as_view()),
    
    path('readcreateitem/', ReadCreateItem.as_view()),
    path('readsingleupdateitem/<int:pk>/',ReadSingleUpdateItem.as_view()),
    path('readsingledeleteitem/<int:pk>/',ReadSingleDeleteItem.as_view()),
    path('readupdatedeleteitem/<int:pk>/',ReadUpdateDeleteItem.as_view())
    
    
    
]
