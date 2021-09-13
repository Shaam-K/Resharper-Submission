from crud_app.models import table_contents
from django import forms

class create_form(forms.ModelForm):

    class Meta:
        model = table_contents
        fields = '__all__'

