from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

from .DiscountRequestAdapter import *
from .application.DiscountService import DiscountService
from .serializers import DiscountPostSerializer


class Discounts(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    pagination_class = LimitOffsetPagination
    queryset = Discount.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['valid_date_start', 'valid_date_end']
    filterset_fields = ['code', 'valid_date_start', 'valid_date_end', 'status']
    search_fields = ['code', 'valid_date_start', 'valid_date_end', 'status']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.discount_request_adapter = DiscountRequestAdapter()
        self.discount = DiscountService()

    def post(self, request) -> Response:
        discount_data = DiscountPostSerializer(data=request.data)

        if not discount_data.is_valid():
            return Response({"message": "Not Valid"}, status=status.HTTP_400_BAD_REQUEST)

        code, cart_number, cart_amount = self.discount_request_adapter.adapt_serializer_data(discount_data)

        return self.discount.response_client_service(
            code,
            cart_number,
            cart_amount
        )
         
