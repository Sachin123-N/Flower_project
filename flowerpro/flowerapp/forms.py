from django import forms
from .models import Flower


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"

        widgets = {
            "flower_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "flower_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "flat_delivery_date": forms.DateInput({type: "Date"}),
            "payment_mode": forms.Select(attrs={'class': 'class-controls'}),
            "flower_quantity": forms.Select(attrs={'class': 'class-controls'}),
        }
