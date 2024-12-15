from django.urls import path,include
from apps.productmodule import views


urlpatterns = [
    path('',views.index,name='index'),
    path('list',views.list,name='list'),
    path('add',views.add,name='add'),
    path('search',views.search,name='search'),
    path('show<id>',views.show,name='show'),
    path('delete<id>',views.delete,name='delete'),
    path('edit<id>',views.edit,name='edit'),
]