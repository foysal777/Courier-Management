from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myauth.urls')),

]
# POST /api/users/ → Register
# POST /api/token/ → Login (get token)
# GET /api/users/profile/ → View profile
# POST /api/orders/ → Create order
# GET /api/orders/my_orders/ → View user's orders
# POST /api/orders/{id}/pay_order/ → Get Stripe client_secret
# PATCH /api/orders/{id}/assign_order/ → Admin assigns delivery man
# GET /api/orders/my_assigned_orders/ → Delivery man's orders
# PATCH /api/orders/{id}/update_status/ → Delivery man updates status