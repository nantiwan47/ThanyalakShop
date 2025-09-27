from django.urls import path
from .views import product_detail, add_to_cart, update_cart, delete_cart, cart_detail, search_results, home, checkout, \
    order_status_view, user_logout, register, user_login, profile, edit_profile, admin_login, admin_logout, \
    admin_dashboard, \
    product_list, product_add, product_edit, product_delete, admin_register, order_list, order_update_status, order_detail

urlpatterns = [
    path('', home, name='home'),


    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),


    path('admin-register/', admin_register, name='admin_register'),
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),


    path('search/', search_results, name='search_results'),
    path('product/<int:pk>/', product_detail, name='product_detail'),


    path('cart/', cart_detail, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/<int:pk>/', update_cart, name='update_cart'),
    path('delete-cart/<int:pk>/', delete_cart, name='delete_cart'),


    path("checkout/", checkout, name="checkout"),
    path('order-status/', order_status_view, name='order_status'),


    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/products/', product_list, name='product_list'),
    path('admin/add/', product_add, name='product_add'),
    path('admin/edit/<int:pk>', product_edit, name='product_edit'),
    path('admin/delete/<int:pk>', product_delete, name='product_delete'),

    path('admin/orders/', order_list, name='order_list'),
    path('admin/orders/<int:pk>/', order_detail, name='order_detail'),

    path('admin/orders/<int:pk>', order_update_status, name='order_update_status'),
]
