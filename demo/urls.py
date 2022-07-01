from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from .models.personne import Personne
from .views import home, personne

urlpatterns = [
    path("", home.index, name="home"),
    # personnes
    path("personnes", personne.personne_list, name="personnes"),
    path("personnes/create", personne.CreatePersonne.as_view(), name="create_personne"),
    path("personnes/update/<int:pk>/", personne.UpdatePersonne.as_view(), name="update_personne"),
    path("personnes/<int:pk>/", login_required(DetailView.as_view(model=Personne, template_name="demo/personne/personne_details.html")), name="details_personne"),

]
