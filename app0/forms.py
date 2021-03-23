from django import forms



class UserForm(forms.Form):

        name = forms.CharField(
        label='Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )
        
        carNumber= forms.CharField(
        label='CarNumber',
        max_length=8,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )



        cin= forms.CharField(
        label='CIN',
        max_length=8,
        min_length=8,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),

        )
        phone = forms.CharField(
        label='Name',
        max_length=12,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )

        fields = "__all__"


