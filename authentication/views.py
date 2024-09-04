from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .serializers import UserRegistrationSerializers
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.permissions import IsAuthenticated
from .models import UserRegisterModel

class RegisterView(APIView):
    def post(self, request):
        # This will register user
        try:
            data = request.data
            # not used get method because if any error come automatically will go in exception
            password = data['password']
            confirm_password = data["confirm_password"]
            # Handling the case when we received null from frontend
            if (password == None or confirm_password == None):
                return {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message":"Password or Confirm Password can't be none"
                }
            serializers = UserRegistrationSerializers(data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response({
                "status":status.HTTP_201_CREATED,
                "message":"User has been register succesfully"
            })
        except KeyError as e:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message" : str(e)
            })
        except IntegrityError as e:
            return Response({
                "status":status.HTTP_409_CONFLICT,
                "message" : str(e)
            })
        except Exception as e:
            return Response({
                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message" : str(e)
            })

    # After login we will generate the JWT token for user and than validate all the api on the basis of that token
class LoginView(APIView):
    def post(self, request):
        # this will login the user
        data = request.data
        user = authenticate(data)
        if user is None:
            return Response({
                "status":status.HTTP_401_UNAUTHORIZED,
                "message":"credentials doesn't match"
            })
        access_token = AccessToken.get_token_backend(data)
        refresh_token = RefreshToken.get_token_backend(data)
        
        return Response({
            "access_token": access_token,
            "refresh_token": refresh_token
        })
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
 
        user_id = request.user.id
        user_obj = UserRegisterModel.objects.get(id = user_id)
        serializer = UserRegistrationSerializers(user_obj)
        return Response(serializer.data)



