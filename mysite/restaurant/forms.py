# restaurant/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PedidoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=255)
    email = forms.EmailField(label='Correo Electrónico')

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Hacer Pedido'))
