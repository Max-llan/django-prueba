from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre','telefono','email','direccion']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'ejemplo@dominio.com'}),
            'telefono': forms.TextInput(attrs={'placeholder':'+56 9 1234 5678'}),
        }

    def clean_telefono(self):
        tel = self.cleaned_data.get('telefono', '').strip()
        import re
        if tel and not re.match(r'^[\d+\-\s()]+$', tel):
            raise forms.ValidationError("Teléfono contiene caracteres inválidos.")
        return tel
