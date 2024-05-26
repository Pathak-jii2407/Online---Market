from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('login/', views.login_page, name='login'),
    path('account/', views.account_page, name='account'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('payment_process/', views.payment_process, name='payment_process'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
