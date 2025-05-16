from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def home(request):
    phone_number= "0707435635"
    amount = 2000
    client = MpesaClient()
    response = client.stk_push(phone_number,amount, "XYZ", "Transport", "https://example.com")
    return HttpResponse("SUCCESSFUL")