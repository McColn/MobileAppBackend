# yourapp/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, CustomUserCreateView, CustomAuthTokenView, CustomUserUpdateView, CustomUserDeleteView, CustomUserListView,LogoutAPIView

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    # Your other URL patterns
    path('api/', include(router.urls)),
    path('api/register/', CustomUserCreateView.as_view(), name='create_user'),
    path('api/login/', CustomAuthTokenView.as_view(), name='login'),

    path('api/update-user/<int:pk>/', CustomUserUpdateView.as_view(), name='update-user'),
    path('api/delete-user/<int:pk>/', CustomUserDeleteView.as_view(), name='delete_user'),
    path('api/list-user/', CustomUserListView.as_view(), name='list_user'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
]
