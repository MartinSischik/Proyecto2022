from django.forms import*

from core.models import CateQuimico, Quimico

class CateQuimicoForm(ModelForm):
    class Meta:
        model = CateQuimico
        fields = '__all__'
        labels = {
                'name':'Descripcion'
            }
        widgets = {
            'name': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'cosas',
                        
                }
            )
        }

class QuimicoForm (ModelForm):
    class Meta:
        model = Quimico
        fields = '__all__'
        labels = {
                'nombre':'Nombre'
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'categoria': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'ingrediente': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'cantidad': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'unidades': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            )
            
        }