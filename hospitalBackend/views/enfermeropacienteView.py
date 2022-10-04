from turtle import update
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.enfermeropacienteSerializer import EnfermeroPacienteSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario
from hospitalBackend.models.enfermeropaciente import EnfermeroPaciente


class EnfermeroPacienteListCreateView(generics.ListCreateAPIView):  
    queryset = EnfermeroPaciente.objects.all()
    serializer_class = EnfermeroPacienteSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los EnfermeroPaciente")
        queryset = self.get_queryset()
        serializer = EnfermeroPacienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("Post a EnfermeroPaciente")  
        print(request.data)

        usuarioData = request.data.pop('usuario')
        serializerU = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save() 

        epData = request.data        
        epData = update({"usuario":usuario.id})
        serializerEp = EnfermeroPacienteSerializer(data=epData)
        serializerEp.is_valid(raise_exception=True)
        serializerEp.save() 
        return Response(status=status.HTTP_201_CREATED) 

class EnfermeroPacienteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnfermeroPaciente.objects.all()
    serializer_class = EnfermeroPacienteSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a EnfermeroPaciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a EnfermeroPaciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a EnfermeroPaciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)