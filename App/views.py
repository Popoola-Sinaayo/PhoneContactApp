from xml.dom.minidom import parseString
from django.shortcuts import render
from .models import Phone
from .serializers import PhoneSerializer
from rest_framework.views import Response
from rest_framework.views import APIView, status

# Create your views here.


def index(request):
    return render(request, 'index.html')


class ListView(APIView):
    def get(self, request, format=None):
        phones = Phone.objects.all()
        phones_object = PhoneSerializer(phones, many=True)
        return Response(phones_object.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        phone_object = PhoneSerializer(data=request.data)
        if phone_object.is_valid():
            firstname = request.data['firstname']
            lastname = request.data['lastname']
            number = request.data['number']
            queryname = Phone.objects.filter(firstname=firstname)
            querynumber = Phone.objects.filter(number=number)
            if len(queryname) > 0 or len(querynumber) > 0:
                return Response({'message': 'name or number already exist'}, status=status.HTTP_400_BAD_REQUEST)
            phone_object.save()
            return Response(phone_object.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        number = request.data['number']
        try:
            phone = Phone.objects.get(firstname=firstname)
        except Phone.DoesNotExist:
            phone_number = Phone.objects.get(number=number)
            phone_number.firstname = firstname
            phone_number.lastname = lastname
            phone_number.save()
            return Response(PhoneSerializer(phone_number).data, status=status.HTTP_200_OK)
        phone.number = number
        phone.save()
        return Response(PhoneSerializer(phone).data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        firstname = request.data['firstname']
        print(firstname)
        phone = Phone.objects.get(firstname=firstname)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
