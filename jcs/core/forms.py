from django.forms import *

from core.models import *
from django.db.models import Q


class CateQuimicoForm(ModelForm):
    class Meta:
        model = CateQuimico
        fields = '__all__'
        labels = {

        }
        widgets = {
            'nombre': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre de Categoria',

                       }
            )
        }

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data


class QuimicoForm (ModelForm):
    # procedencia = ModelChoiceField(queryset=Proveedor.objects.none(), widget=Select(attrs={
    #     'class': 'form-control select2',
    #     'style': 'width: 100%'
    # }))
    class Meta:
        model = Quimico
        fields = '__all__'
        labels = {

        }
        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',

                       }
            ),
            'categoria': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Categoria',
                       'id': 'select1'
                       }
            ),
            'ingrediente': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Descripcion',

                       }
            ),
            'cantidad': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Cantidad',

                       }
            ),
            'unidades': Select(
                attrs={'class': 'form-control',
                       'placeholder': '1',
                       'id': 'select2'
                       }
            ),
            'precio': TextInput(
                attrs={'class': 'form-control ',
                       'placeholder': 'preio',
                       # 'id':'select3'
                       }
            ),
            'procedencia': Select(
                attrs={'class': 'form-control select2',
                       'placeholder': 'Procedencia',
                       'id': 'select3'
                       }
            ),
        }


class SumaQuimicoForm (ModelForm):

    Nombre = ModelChoiceField(queryset=Quimico.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    class Meta:
        model = Quimico
        fields = '__all__'
        labels = {

        }
        widgets = {
            'cantidad': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Cantidad',

                       }
            ),
            'precio': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'precio',

                       }
            ),
        }
        exclude = ['procedencia',
                   'unidades', 'ingrediente', 'categoria', 'name']


class GranoForm (ModelForm):
    class Meta:
        model = Grano
        fields = '__all__'
        labels = {


        }
        widgets = {
            'nombre': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',

                       }
            ),
            'variedad': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Variedad',

                       }
            ),
            'stock': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Cantidad de Kilogramos',

                       }
            ),
            'precio': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Precio de compra',

                       }
            ),
            'Procedencia': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Procedencia',
                       'id': 'select1'
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
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',

                       }
            ),
            'ubicacion': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ubicacion',

                       }
            ),
            'hectareas': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ingrediente',

                       }
            ),
            'trabajos': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Cantidad',

                       }
            ),
            'gasto': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Unidades de medida',

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
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',
                       'name': 'Nombre'

                       }
            ),
            'chapa': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Chapa',


                       }
            ),
            'cedula': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Cedula',

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
            'cliente': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Cantidad',
                       'id': 'select1'
                       }
            ),
            'camion_id': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',
                       'id': 'select2'
                       }
            ),
            'grano_id': Select(
                attrs={'class': 'form-control',
                       # 'placeholder':'Ubicacion',
                       'id': 'select3'

                       }
            ),

            'cantidad': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Unidades de medida',

                       }
            ),

            'fecha': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',


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
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',
                       'name': 'Nombre'

                       }
            ),
            'telefono': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Telefono',


                       }
            ),
            'ruc': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ruc',

                       }
            ),
            'email': EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Email',

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
            'name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',
                       'name': 'Nombre'

                       }
            ),
            'telefono': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Telefono',


                       }
            ),
            'ruc': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Ruc',

                       }
            ),
            'email': EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Email',

                       }
            ),

        }


class ProduccionForm (ModelForm):
    # producto=ModelChoiceField(queryset=Quimico.objects.filter(Q(categoria_id=8)| Q (categoria_id=5)),
    # widget=Select(attrs={'class':'form-control select2','style':'width 100%','id':'select2'},))
    class Meta:
        model = Produccion
        fields = '__all__'
        labels = {

        }
        widgets = {
            'parcela': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Parcela',
                       'id': 'select1'
                       }
            ),
            'producto': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Ubicacion',
                       'id': 'select2'

                       }
            ),

            'cantidad': NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Unidades de medida',

                       }
            ),

            'fecha': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',


                }
            )

        }


class TrabajoForm (ModelForm):
    # nombre=ModelChoiceField(queryset=Quimico.objects.none(),widget=Select(attrs={'class':'form-control select2','style':'width 100%'}))
    class Meta:
        model = Trabajo
        fields = '__all__'
        labels = {


        }
        widgets = {
            'empleado': Select(
                attrs={'class': 'form-control',
                       'placeholder': '',
                       'id': 'select3',
                       'style': "width:100%",
                       }
            ),
            'parcela': Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Parcela',
                       'id': 'select1',
                       'style': "width:100%"

                       }
            ),
            'tipo': Select(
                attrs={'class': 'form-control',
                       'placeholder': '',
                       'id': 'select2',
                       'style': "width:100%",
                       }
            ),
            'hectareas': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Hectareas',

                       }
            ),
            'descripcion': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Descripcion',

                       }
            ),
            'gasto': TextInput(
                attrs={'readonly': True,
                       'placeholder': 'Gastos',
                       'class': 'form-control',
                       'background-color': '#2A3038'
                       }
            ),
            'fecha': DateInput(format='%Y-%m-%d',
                               attrs={
                                   'type': 'date',
                                   'class': 'form-control',
                                   'value': datetime.now().strftime('%Y-%m-%d'),

                               }
                               )

        }


class EmployeeForm (ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {


        }
        widgets = {
            'type': Select(
                attrs={'class': 'form-control',
                       'id': 'select1',
                       'style': "width:100%"

                       }
            ),
            'name': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre',
                       'name': 'Nombre'

                       }
            ),
            'ci': TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Telefono',


                       }
            ),

            'email': EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Email',

                       }
            ),

        }
