from django import forms


class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    #fecha = forms.DateTimeField(default=datetime.date.today, null=True, blank=True, verbose_name="Fecha")
    fecha = forms.DateField(label="Fecha Nacimiento", input_formats= ["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    edad =forms.IntegerField(label='Edad', max_value=99)
class ActualizarPersonaForm(PersonaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")