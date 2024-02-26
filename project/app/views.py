# views.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book,CustomUser
from .serializers import BookSerializer
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)



class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.AllowAny,)

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)


class CustomUserDeleteView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

class CustomUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

class CustomAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            # Get or create the Token instance for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})
        except Exception as e:
            # Log the exception or handle it based on your requirements
            return Response({'detail': f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Delete the authentication token
        try:
            request.auth.delete()
        except AttributeError:
            # Handle the case where no token is found
            pass

        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)