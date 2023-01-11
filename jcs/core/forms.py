from django.forms import*

from core.models import *

class CateQuimicoForm(ModelForm):
    class Meta:
        model = CateQuimico
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre de Categoria',
                        
                }
            )
        }

class QuimicoForm (ModelForm):
    class Meta:
        model = Quimico
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'categoria': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Categoria',
                        
                }
            ),
            'ingrediente': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ingrediente',
                        
                }
            ),
            'cantidad': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad',
                        
                }
            ),
            'unidades': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Unidades de medida',
                        
                }
            )
            
        }

class GranoForm (ModelForm):
    class Meta:
        model = Grano
        fields = '__all__'
        labels = {
                
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'variedad': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Variedad',
                        
                }
            ),
            'stock': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad de Kilogramos',
                        
                }
            ),
            'precio': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Precio de compra',
                        
                }
            ),
            'Procedencia': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Procedencia',
                        
                }
            ),
            
        }

class ParcelaForm (ModelForm):
    class Meta:
        model = Parcelas
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'ubicacion': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ubicacion',
                        
                }
            ),
            'hectareas': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ingrediente',
                        
                }
            ),
            'trabajos': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad',
                        
                }
            ),
            'gasto': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Unidades de medida',
                        
                }
            )
            
        }

class CamionForm (ModelForm):
    class Meta:
        model = camion
        fields = '__all__'
        labels = {
                
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        'name':'Nombre'
                        
                }
            ),
            'chapa': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Chapa',
                        
                        
                }
            ),
            'cedula': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Cedula',
                        
                }
            ),
            
        }
        

class EntregasForm (ModelForm):
    class Meta:
        model = Entregas
        fields = '__all__'
        labels = {
                
            }
        widgets = {
            'camion_id': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        
                }
            ),
            'grano_id': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Ubicacion',
                        
                }
            ),
            
            'cantidad': NumberInput(
                attrs= {'class':'form-control',
                        'placeholder':'Unidades de medida',
                        
                }
            ),
            'cliente': Select(
                attrs= {'class':'form-control',
                        'placeholder':'Cantidad',
                        
                }
            )
            
        }

class ClienteForm (ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
                
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        'name':'Nombre'
                        
                }
            ),
            'telefono': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Telefono',
                        
                        
                }
            ),
            'ruc': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ruc',
                        
                }
            ),
            'email': EmailInput(
                attrs= {'class':'form-control',
                        'placeholder':'Email',
                        
                }
            ),
            
        }

class ProveedorForm (ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        labels = {
                
                
            }
        widgets = {
            'nombre': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Nombre',
                        'name':'Nombre'
                        
                }
            ),
            'telefono': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Telefono',
                        
                        
                }
            ),
            'ruc': TextInput(
                attrs= {'class':'form-control',
                        'placeholder':'Ruc',
                        
                }
            ),
            'email': EmailInput(
                attrs= {'class':'form-control',
                        'placeholder':'Email',
                        
                }
            ),
            
        }


