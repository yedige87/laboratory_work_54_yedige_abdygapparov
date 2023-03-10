from django.urls import path

from shop_app.views.base import index_view
from shop_app.views.products import product_view, categories_view, category_add_view, product_add_view, \
    category_edit_view, product_edit_view, category_delete_view, product_delete_view

urlpatterns = [
    path("", index_view, name='index'),
    path('products', index_view, name='index'),
    path('products/<int:pk>', product_view, name='product_view'),
    path('categories', categories_view, name='categories_view'),
    path('categories/add', category_add_view, name='category_add'),
    path('products/add', product_add_view, name='product_add'),
    path('category/<int:pk>/edit', category_edit_view, name='category_edit'),
    path('product/<int:pk>/edit', product_edit_view, name='product_edit'),
    path('category/<int:pk>/delete', category_delete_view, name='category_delete'),
    path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
]
