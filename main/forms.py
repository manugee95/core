from django import forms 
from .models import Career

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['first_name', 'last_name', 'phone', 'address', 'email', 'city', 'state', 'zip', 
        'cell_number', 'position_applied', 'state_applied', 'shift_applied_dc', 'shift_applied_maryland', 'shift_applied_virginia', 
        'resume', 'message']