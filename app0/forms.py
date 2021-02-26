from django import forms



class UserForm(forms.Form):

        name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )
        
        carNumber= forms.CharField(
        label='CarNumber',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )
