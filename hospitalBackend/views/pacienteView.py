from turtle import update
from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalBackend.serializers.pacienteSerializer import PacienteSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario
from hospitalBackend.models.paciente import Paciente


class PacienteListCreateView(generics.ListCreateAPIView):  
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Paciente")
        queryset = self.get_queryset()
        serializer = PacienteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("Post a Paciente")  
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save() 
        paData = request.data        
        paData = update({"usuario":usuario.id})
        serializerPa = PacienteSerializer(data=paData)
        serializerPa.is_valid(raise_exception=True)
        serializerPa.save() 
        return Response(status=status.HTTP_201_CREATED) 

class PacienteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Paciente")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)

# from rest_framework import status
# from rest_framework.response import Response
# from hospitalBackend.models.paciente import Paciente
# from hospitalBackend.serializers.pacienteSerializer import PacienteSerializer
# from rest_framework.decorators import api_view

# @api_view(['GET','POST'])
# def createpaciente(request):
#     if request.method == 'GET':
#         modelo=Paciente.objects.all()
#         serializer=PacienteSerializer(modelo, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer=PacienteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# @api_view(['PUT','DELETE'])
# def detailpaciente(request,pk):
#     if request.method =='PUT':
#         modelo=Paciente.objects.get(pk=pk)
#         serializer=PacienteSerializer(modelo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#     elif request.method == 'DELETE':
#         modelo=Paciente.objects.get(pk=pk)
#         modelo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

