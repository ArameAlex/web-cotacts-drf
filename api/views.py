from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
 #serializer
from base.models import Contacts
from .serializers import Contacts_serializer, User_serializer
# geting users
from django.contrib.auth import get_user_model
# log in
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

User = get_user_model()


#region function

@api_view(['GET'])
def getpageData(request, page):
    from_one = (page-1)
    startat = (from_one * 5)
    end_at = ((from_one * 5) + 5)
    person = Contacts.objects.order_by("-id")[startat:end_at]
    serializer = Contacts_serializer(person, many=True)
    return Response(serializer.data)

#endregion

#region mixin

class ContactsListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Contacts.objects.order_by("-id").all()
    serializer_class = Contacts_serializer

    def get(self, request:Request):
        return self.list(request)

    def post(self, request:Request):
        return self.create(request)

class ContactsDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.GenericAPIView):

    queryset = Contacts.objects.order_by("-id")
    serializer_class = Contacts_serializer

    def get(self, request:Request, pk):
        return self.retrieve(request, pk)

    def put(self, request:Request, pk):
        return self.update(request, pk)

    def delete(self, request:Request, pk):
        return self.destroy(request, pk)


#endregion

#region generic_views

class ContactsListGenerics(generics.ListCreateAPIView):
    queryset = Contacts.objects.order_by("-id").all()
    serializer_class = Contacts_serializer

class ContactsDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.order_by("-id").all()
    serializer_class = Contacts_serializer

#endregion

#region view_set

class ContactsViewset(viewsets.ModelViewSet):
    queryset = Contacts.objects.order_by("-id").all()
    serializer_class = Contacts_serializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

#endregion

#region userview

class UserGenericAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User_serializer

#endregion
