from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Auto
from .serializers import AutoSerializer

class AutoViewset(viewsets.ModelViewSet):
  queryset = Auto.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = AutoSerializer
  
  def get_queryset(self):
    queryset = Auto.objects.all()
    tipo = self.request.query_params.get('tipo', None)
    if tipo:
      queryset = queryset.filter(tipo=tipo)
      
    order_precio = self.request.query_params.get('precio', None)
    if order_precio:
      if order_precio == 'asc':
        queryset = queryset.order_by('precio')
      elif order_precio == 'desc':
        queryset = queryset.order_by('-precio')
        
    order_anio = self.request.query_params.get('anio', None)
    if order_anio:
      if order_anio == 'asc':
        queryset = queryset.order_by('anio')
      elif order_anio == 'desc':
        queryset = queryset.order_by('-anio')        
      
    return queryset
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response({"mensaje": "Auto Agregado Correctamente", "auto": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response({"mensaje": "Auto Actualizado Correctamente", "auto": serializer.data})

  def destroy(self, request, *args, **kwargs):
    instance = self.get_object()
    self.perform_destroy(instance)
    return Response({"mensaje": "Auto Eliminado Correctamente"}, status=status.HTTP_204_NO_CONTENT)