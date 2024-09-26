from django import forms  
from models import Order
class OrderForm(forms.Model):

    class Meta:
        model = Order
        fields = ['customer_email']