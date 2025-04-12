from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/add/', views.add_item, name='add_item'),
    path('item/<int:item_id>/status/', views.update_status, name='update_status'),
    path('item/update-order/', views.update_order, name='update_order'),
    path('export/markdown/', views.export_markdown, name='export_markdown'),
    path('export/excel/', views.export_excel, name='export_excel'),
]