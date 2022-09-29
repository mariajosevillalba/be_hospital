from turtle import update
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.historiaSerializer import HistoriaSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario
from hospitalBackend.models.historia import Historia


class HistoriaListCreateView(generics.ListCreateAPIView):  
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Historia")
        queryset = self.get_queryset()
        serializer = HistoriaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("Post a Historia")  
        print(request.data)

        usuarioData = request.data.pop('usuario')
        serializerU = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save() 

        hisData = request.data        
        hisData = update({"usuario":usuario.id})
        serializerHis = HistoriaSerializer(data=hisData)
        serializerHis.is_valid(raise_exception=True)
        serializerHis.save() 
        return Response(status=status.HTTP_201_CREATED) 

class HistoriaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Historia")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Historia")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Historia")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)