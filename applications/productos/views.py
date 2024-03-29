from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (
    Productos,
    TipoProducto,
)
from .serializers import (
    AllProductsSerializer,
    AllTypeProductsSerializer,
)
# Authorization
# from applications.users.authentications_mixins import Authentication

# Create your views here.
class ListaProductos(viewsets.ModelViewSet):
    serializer_class = AllProductsSerializer
    
    queryset = Productos.objects.all()
    
    # def get_queryset(self, pk=None):
    #     if pk is None:
    #         return self.get_serializer().Meta.model.objects.filter(state=True)
    #     return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    # def list(self, request):
    #     for key, value in request.__dict__.items():
    #         print(key, '==', value)
    #     product_serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(product_serializer, status=status.HTTP_200_OK)

    """
    def create(self, request):
        # send information to serializer 
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = ProductRetrieveSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            data = validate_files(request.data, 'image', True)
            product_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    """

class ListaTipoProductos(viewsets.ModelViewSet):
    serializer_class = AllTypeProductsSerializer
    
    queryset = TipoProducto.objects.all()