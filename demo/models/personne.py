from django.core.validators import RegexValidator
from django.db import models


class Personne(models.Model):
    date_mise_a_jour = models.DateField(verbose_name="Date de mise à jour", auto_now=True)
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    addresse = models.CharField(max_length=200)
    code_postal_regex = RegexValidator(regex="^(^[0-9]{5}(?:-[0-9]{4})?$|^$)", message="Veuillez entrer un code postal valide")
    code_postal = models.CharField(max_length=5, validators=[code_postal_regex])
    ville = models.CharField(max_length=100)
    telephone_regex = RegexValidator(regex="^\s*\d{10}\s*$", message="Veuillez entrer un numéro de téléphone valide")
    telephone = models.CharField(validators=[telephone_regex], max_length=10)
    date_inscription = models.DateField(verbose_name="Date d'inscription", auto_now_add=True)
    commentaire = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def get_adresse_complete_str(self):
        return f"{self.addresse} \n {self.code_postal} {self.ville}"
