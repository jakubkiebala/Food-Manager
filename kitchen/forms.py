from django import forms


class MagazineAddForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Wprowadź nazwę magazynu'})
    )
    is_cooler = forms.BooleanField(required=False, label='Czy jest lodówką?')
