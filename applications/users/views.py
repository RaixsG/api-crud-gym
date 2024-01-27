from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.
class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            print('Pasó validación')
        return Response({'mensaje': 'Pasó validación'}, status = status.HTTP_200_OK)