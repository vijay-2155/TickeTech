from django import forms
from .models import City, Category, Ticket


class CityForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label="Select a city",
        widget=forms.Select(attrs={'class': 'rounded-md p-2 w-full gradient-dropdown hover-effect'}),
    )




class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # Exclude the museum field since it's set in the view
        fields = ['category', 'customer_name', 'customer_age', 'customer_email', 'customer_phoneno']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-input w-full p-2 border rounded'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-input w-full p-2 border rounded', 'placeholder': 'John Doe'}),
            'customer_age': forms.NumberInput(attrs={'class': 'form-input w-full p-2 border rounded', 'placeholder': '30', 'min': '0'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-input w-full p-2 border rounded', 'placeholder': 'email@example.com'}),
            'customer_phoneno': forms.NumberInput(attrs={'class': 'form-input w-full p-2 border rounded', 'placeholder': '1234567890'}),
        }
