from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from .emails import send_otp


class UserRegistraion(APIView):
    def post(self, request):
        try:
            serializer= CustomUserSerializer(data = request.data)
            if serializer.is_valid():
                user = serializer.save()
                send_otp(serializer.data['email'])
                return Response({
                    'status':200,
                    'message':'Account registred successfully',
                    'data':serializer.data['email'],
                })
            return Response({
                'status':400,
                'message':'Something went wrong',
                'data':serializer.errors,
            })

        except Exception as e:
            return Response({
                'status':400,
                'message':f'Something went wrong with error message {e}',
                'data':serializer.errors,
            })

# class VerifyOTP(APIView):  # New class for OTP verification
#     def post(self, request):
#         otp = request.data.get('otp')
#         email = request.data.get('email')
        
#         try:
#             user = CustomUser.objects.get(email=email)  # Fetch user by email
#             if user.otp == otp:  # Assuming you have an otp field in your User model
#                 user.is_verified = True  # Assuming you have an is_verified field
#                 user.save()
#                 return Response({
#                     'status': 200,
#                     'message': 'OTP verified successfully',
#                 })
#             return Response({
#                 'status': 400,
#                 'message': 'Invalid OTP',
#             })
#         except User.DoesNotExist:
#             return Response({
#                 'status': 404,
#                 'message': 'User not found',
#             })
#         except Exception as e:
#             return Response({
#                 'status': 400,
#                 'message': f'Something went wrong with error message {e}',
#             })

# Create your views here.
