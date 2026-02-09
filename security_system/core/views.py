from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from .serializers import UserCreateSerializer
from .models import UserApplicationAccess, User
from .serializers import (
    UserAccessSerializer,
    UserSerializer
)
from .permissions import IsAdmin

# =========================
# USUARIO AUTENTICADO
# =========================

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# ❌ FUNCIONALIDAD VISUAL ROTA (lista vacía)
class MyApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # ERROR INTENCIONAL
        accesses = UserApplicationAccess.objects.filter(id=request.user.id)
        serializer = UserAccessSerializer(accesses, many=True)
        return Response(serializer.data)

# =========================
# ADMIN
# =========================

class UsersListView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdmin]

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserApplicationsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, id):
        accesses = UserApplicationAccess.objects.filter(user_id=id)
        serializer = UserAccessSerializer(accesses, many=True)
        return Response(serializer.data)

# ❌ FUNCIONALIDAD VISUAL ROTA (error pero guarda)
class GrantAccessView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        user_id = request.data.get('user_id')
        app_id = request.data.get('app_id')

        UserApplicationAccess.objects.create(
            user_id=user_id,
            application_id=app_id
        )

        return Response(
            {"error": "No se pudo asignar el acceso"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# =========================
# APLICACIONES EXTERNAS
# =========================

class CheckAccessView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        app_code = request.query_params.get('app_code')

        has_access = UserApplicationAccess.objects.filter(
            user=request.user,
            application__code=app_code
        ).exists()

        return Response({
            "has_access": has_access
        })
