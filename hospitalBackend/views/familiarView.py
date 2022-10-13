from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.backends import TokenBackend

from hospitalBackend.serializers.familiarSerializer import FamiliarSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario
from hospitalBackend.models.familiar import Familiar


class FamiliarListCreateView(generics.ListCreateAPIView):  
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Familiar")
        queryset = self.get_queryset()
        serializer = FamiliarSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("Post a Familiar")  
        print(request.data)

        usuarioData = request.data.pop('usuario')
        serializerU = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save() 

        famData = request.data        
        famData.update({"usuario":usuario.id})
        serializerFam = FamiliarSerializer(data=famData)
        serializerFam.is_valid(raise_exception=True)
        serializerFam.save() 
        return Response(status=status.HTTP_201_CREATED) 

class FamiliarRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Familiar")

        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)

        # if valid_data['user_id'] != kwargs['pk']:
        #     stringResponse = {'detail':'Unauthorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Familiar")

        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)

        # if valid_data['user_id'] != kwargs['pk']:
        #     stringResponse = {'detail':'Unauthorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
         
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Familiar")

        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        # tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        # valid_data = tokenBackend.decode(token,verify=False)

        # if valid_data['user_id'] != kwargs['pk']:
        #     stringResponse = {'detail':'Unauthorized Request'}
        #     return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().delete(request, *args, **kwargs)