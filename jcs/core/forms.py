from django.forms import ModelForm

from core.models import CateQuimico

class CateQuimicoForm(ModelForm):
    class Meta:
        model = CateQuimico
        fields = '__all__'