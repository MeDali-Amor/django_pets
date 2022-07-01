from enum import Enum
from django.core.validators import RegexValidator
from django.db import models

from demo.models.personne import Personne


class TypeAnimalChoise(Enum):
    LAPIN="Lapin"
    CHINCHILA="Chinchila"
    CHIEN='Chien'
    CHAT='Chat'
  
class SexChoice(Enum):
    F = "Féminin"
    M = "MAsculain"
    NI = "Non identifié"

class EmplacementChoice(Enum):
    PENSION="Pension"
    REFUGE='Refuge'

class OuiNonChoice(Enum):
    OUI="Oui"
    NON="Non"

class Animal(models.Model):
    nom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(verbose_name="date de naissance", null=True, blank=True)
    date_de_mise_a_jour = models.DateField(verbose_name="date de mise à jour", auto_now=True)
    date_arrive = models.DateField(verbose_name="date de première  arrivée", null=True, blank=True)
    type_animal = models.CharField(max_length=30,verbose_name="Type d'animal",choices=[(tag.name, tag.value) for tag in TypeAnimalChoise])
    emplacement = models.CharField(max_length=30,verbose_name="Emplacement",choices=[(tag.name, tag.value) for tag in EmplacementChoice])
    sexe = models.CharField(max_length=30,verbose_name="Sexe",choices=[(tag.name, tag.value) for tag in SexChoice])
    sterilise = models.CharField(max_length=30, verbose_name="Stérilisé",choices=[(tag.name, tag.value) for tag in OuiNonChoice])
    vaccine = models.CharField(max_length=30, verbose_name="vaccine",choices=[(tag.name, tag.value) for tag in OuiNonChoice])
    date_dernier_vaccin = models.DateField(verbose_name="date de dernier rappel de vaccin", null=True, blank=True)
    date_sterilisation = models.DateField(verbose_name="date de sterilisation", null=True, blank=True)
    proprietaire = models.ForeignKey(
        Personne,
        verbose_name="Propiétaire (à repmlir uniquement si animal de la pension",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    inactif = models.BooleanField(default=False,
    verbose_name="Desactivé (Ne cocher qui si vous ne souhaitez\ plus gérer cet animal dans l'application) ")
    description  = models.CharField(max_length=2000, blank=True)
    def __str__(self) :
        return f"{self.get_type_animal_display()} {self.nom}"
    def is_from_pension(self):
        return self.emplacement == EmplacementChoice.PENSION.name
    def is_from_refuge(self):
        return self.emplacement == EmplacementChoice.REFUGE.name

    def get_vaccin_str(self):
        if self.date_dernier_vaccin:
            return (
                str(self.get_vaccine_display()) + "(dernier rappel le " + self.date_dernier_vaccin.strftime("%d/%m/%Y") + ")"

            )
        else:
            return self.get_vaccine_display