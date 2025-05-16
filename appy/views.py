from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient

from appy.models import Payment


# Create your views here.
def home(request):
    phone_number= "0707435635"
    amount = 1
    client = MpesaClient()
    response = client.stk_push(phone_number, amount, "XYZ", "Transport", "https://example.com")
    m_id = response.merchant_request_id
    c_id = response.checkout_request_id
    Payment.objects.create(phone_number=phone_number, amount=amount, m_id=m_id, c_id=c_id, status="Started")
    return HttpResponse(response)


# pip install django-daraja