from rest_framework.response import Response
from .serializer import StateSerializer, UserManagerSerializer
from rest_framework.views import APIView
from rest_framework import status

from .models import UserManager
from django.utils import timezone

class UserManagerAPI(APIView):

    # Post.
    def post(self, request):
        data_serializer = request.data
        data_serializer['created_at'] = timezone.now()
        data_serializer['updated_at'] = timezone.now()
        serializer = UserManagerSerializer(data=data_serializer)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'success': True,
                'data': user.username
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    # Post.
    def put(self, request, slug):
        try:
            user_update = UserManager.objects.get(username=request.data['username'])
            user_update.updated_at = timezone.now()
            serializer = UserManagerSerializer(data=user_update)
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    'success': True,
                    'data': user.username
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': False,
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'errors': str(e)
            }, status=status.HTTP_404_NOT_FOUND)
