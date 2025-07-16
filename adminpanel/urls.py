from django.urls import path
from adminpanel import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),

    path('', views.admin_dashboard, name='admin_dashboard'),
    path('your-admin-logout/', views.admin_logout, name='admin_logout'),  # 
    path('categories/', views.manage_categories, name='manage_categories'),
    path('categories/add/', views.product_add_category, name='add_category'),
    path('categories/update/<int:category_id>/', views.product_update_category, name='update_category'),
    path('categories/delete/<int:category_id>/', views.product_delete_category, name='delete_category'),

    path('subcategories/', views.product_manage_subcategories, name='manage_subcategories'),
    path('subcategories/add/', views.product_add_subcategory, name='add_subcategory'),
    path('subcategories/update/<int:subcategory_id>/', views.product_update_subcategory, name='update_subcategory'),
    path('subcategories/delete/<int:subcategory_id>/', views.product_delete_subcategory, name='delete_subcategory'),

    path('products/', views.manage_products, name='manage_products'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/update/<int:product_id>/', views.update_product, name='update_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    path('manage_discounts/', views.manage_discounts, name='manage_discounts'),
    path('add_discount/', views.add_discount, name='add_discount'),
    path('update_discount/<int:offer_id>/', views.update_discount, name='update_discount'),
    path('delete_discount/<int:offer_id>/', views.delete_discount, name='delete_discount'),

    path('orders/', views.manage_orders, name='manage_orders'),
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/update/<int:order_id>/', views.update_order, name='update_order'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),

    path('service-categories/', views.manage_service_categories, name='manage_service_categories'),
    path('service-categories/add/', views.add_service_category, name='add_service_category'),
    path('service-categories/edit/<int:pk>/', views.update_service_category, name='update_service_category'),
    path('service-categories/delete/<int:pk>/', views.delete_service_category, name='delete_service_category'),

    path('s_subcategories/', views.service_subcategory_list, name='s_subcategory_list'),
    path('s_subcategories/add/', views.service_add_edit_subcategory, name='s_add_subcategory'),
    path('s_subcategories/edit/<int:subcategory_id>/',views.service_add_edit_subcategory, name='s_edit_subcategory'),
    path('s_subcategories/delete/<int:subcategory_id>/', views.service_delete_subcategory, name='s_delete_subcategory'),

    path('services/', views.service_list, name='service-list'),
    path('services/add/', views.add_edit_service, name='add-service'),
    path('services/edit/<int:service_id>/',views.add_edit_service, name='edit-service'),
    path('services/delete/<int:service_id>/', views.delete_service, name='delete-service'),

    path('order-items/', views.manage_order_items, name='manage_order_items'),
    path('order-items/delete/<int:order_item_id>/', views.delete_order_item, name='delete_order_item'),

    path('manage_reviews/', views.manage_reviews, name='manage_reviews'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),

    path('manage_user/', views.manage_user, name='manage_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # Delete user

    path('generate_report/', views.generate_report, name='generate_report'),
    path('report/download/',views.download_pdf, name='download_pdf'),
    
    path('stylists/add/', views.add_stylist, name='add_stylist'),
    path('stylists/', views.manage_stylists, name='manage_stylists'),
    path('stylists/update/<int:stylist_id>/', views.update_stylist, name='update_stylist'),
    path('stylists/delete/<int:stylist_id>/', views.delete_stylist, name='delete_stylist'),
    
    path('slots/', views.manage_slots, name='manage_slots'),
    path('slots/add/', views.add_slot, name='add_slot'),
    path('slots/update/<int:slot_id>/', views.update_slot, name='update_slot'),
    path('slots/delete/<int:slot_id>/', views.delete_slot, name='delete_slot'),
    
   
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_add, name='appointment_add'),
    path('appointments/edit/<int:pk>/', views.appointment_edit, name='appointment_edit'),
    path('appointments/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
    
]
