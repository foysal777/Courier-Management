
from .views import stripe_cancel,stripe_success, CreateCheckoutSession,AllOrdersView,assign_order, UpdateOrderStatusView,MyAssignedOrdersView,MyOrdersView,RegisterView ,CustomTokenObtainPairView , UserProfileView, OrderCreateView
from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView


urlpatterns = [

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile-update/', UserProfileView.as_view(), name='user-profile'),
    path('orders/', OrderCreateView.as_view(), name='create-order'),
    path('my_orders/', MyOrdersView.as_view(), name='my-orders'),
    path('my_assigned_orders/', MyAssignedOrdersView.as_view(), name='my-assigned-orders'),
    path('orders/<int:id>/update_status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
    path('all_orders/', AllOrdersView.as_view(), name='all-orders'),
    path('ad/<int:pk>/assign_order/', assign_order, name='assign-order'), 
    path('stripe-payment/', CreateCheckoutSession, name='payment'), 
    path('success/' , stripe_success , name= 'success'),
    path('cancel/' , stripe_cancel , name= 'cancel'),
    
    
]

