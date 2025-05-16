from django.contrib import admin

from appy.models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'amount', 'status', 'created_at']

admin.site.register(Payment, PaymentAdmin)
