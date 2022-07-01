from django.forms import ModelForm, Form, CharField, TextInput

from demo.models.personne import Personne


class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ("nom","prenom","email","addresse","code_postal","ville","telephone","commentaire")
        widgets = { 
            "nom": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "prenom": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "email": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "addresse": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "code_postal": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "ville": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "telephone": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            "commentaire": TextInput(attrs={'style':'width:400px;', 'class':'form-control mx-2'}),
            }


class PersonneSearchForm(Form):
    nom = CharField(max_length=100, required=False, widget=TextInput(attrs={'style':'width:300px;', 'class':'form-control'}))
    prenom = CharField(max_length=100, required=False, widget=TextInput(attrs={'style':'width:300px;', 'class':'form-control'}))
    email = CharField(max_length=100, required=False, widget=TextInput(attrs={'style':'width:300px;', 'class':'form-control'}))
