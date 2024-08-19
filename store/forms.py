from django.forms import ModelForm
from .models import MSG


class MSGForm(ModelForm):
    class Meta:
        model = MSG
        fields = '__all__'