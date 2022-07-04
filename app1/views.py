
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class RejaVs(ModelViewSet):
    queryset = Reja.objects.all()
    s=RejaSer



