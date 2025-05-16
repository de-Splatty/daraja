from django.db import models

# Create your models here.

class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField( max_length=16)
    amount = models.IntegerField()
    code = models.CharField( max_length=10)
    m_id = models.CharField( max_length=100, unique=True)
    c_id = models.CharField( max_length=100, unique=True)
    status = models.CharField( max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payments"
        ordering = ['-created_at']
