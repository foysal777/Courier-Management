from rest_framework import  permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order, User
from .serializers import OrderSerializer,OrderCreateSerializer,UserProfileSerializer,CustomTokenObtainPairSerializer,RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from myauth.permissions import IsDeliveryMan
import stripe
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .permissions import IsDeliveryMans
from .permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        return self.request.user
    
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

   
class MyOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class MyAssignedOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsDeliveryMan]

    def get_queryset(self):
        return Order.objects.filter(assigned_to=self.request.user).order_by('-created_at')
    
class UpdateOrderStatusView(APIView):
    permission_classes = [IsAuthenticated, IsDeliveryMans]

    def patch(self, request, id):
        try:
            order = Order.objects.get(id=id, assigned_to=request.user)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found or not assigned to you."}, status=404)

        new_status = request.data.get("status")
        allowed_statuses = ["pending", "delivered", "complete"]

        if new_status not in allowed_statuses:
            return Response({"error": "Invalid status."}, status=400)

        order.status = new_status
        order.save()

        return Response({"message": "Order status updated successfully."}, status=200)
    

class AllOrdersView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsAdmin])
def assign_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'detail': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

    delivery_id = request.data.get('delivery_id')
    if not delivery_id:
        return Response({'detail': 'delivery_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        delivery_user = User.objects.get(id=delivery_id, role='delivery')
    except User.DoesNotExist:
        return Response({'detail': 'Valid Delivery Man not found.'}, status=status.HTTP_404_NOT_FOUND)

    order.assigned_to = delivery_user
    order.save()

    return Response({'detail': 'Delivery man assigned successfully.'}, status=status.HTTP_200_OK)



stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def CreateCheckoutSession(request):
   

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": 'price_1RdiTU4Ft3OiftBENmAiWovw',
            "quantity": 1,
        }],
        mode="subscription",
        success_url='http://localhost:8000/api/success/',
        cancel_url='http://localhost:8000/api/sucess',
      
    )
    return Response({'checkout_url': session.url})


def stripe_success(request):
    return render(request, 'success.html')

def stripe_cancel(request):
    return render(request, 'cancel.html')