from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import CreateView, UpdateView

from demo.forms.personne import PersonneForm, PersonneSearchForm
from demo.models.personne import Personne

@login_required
def personne_list(request):
    selected = "personnes"
    personne_list = Personne.objects.all()

    if request.method == "POST":
        form = PersonneSearchForm(request.POST)
        if form.is_valid():
            base_url = reverse('personnes')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = PersonneSearchForm()
        nom_form = request.GET.get("nom", "")
        prenom_form = request.GET.get("prenom", "")
        email_form = request.GET.get("email", "")
        if nom_form is not None:
            personne_list = personne_list.filter(nom__icontains=nom_form)
            form.fields['nom'].initial = nom_form
        if prenom_form is not None:
            personne_list = personne_list.filter(prenom__icontains=prenom_form)
            form.fields['prenom'].initial = prenom_form
        if email_form is not None:
            personne_list = personne_list.filter(email__icontains=email_form)
            form.fields['email'].initial = email_form



    # Pagination : 10 éléments par page
    paginator = Paginator(personne_list.order_by('-date_mise_a_jour'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        personne_list = paginator.page(page)
    except EmptyPage:
        # Si on depasse la limite de pages, on prend la derniere
        personne_list = paginator.page(paginator.num_pages())
    return render(request, "demo/personne/personne_list.html", locals())

class CreatePersonne(CreateView, LoginRequiredMixin):
    model = Personne
    form_class = PersonneForm
    template_name = "demo/personne/personne_form.html"
    def get_success_url(self):
        return reverse_lazy("details_personne", kwargs={"pk": self.object.id})

class UpdatePersonne(UpdateView, LoginRequiredMixin):
    model = Personne
    form_class = PersonneForm
    template_name = "demo/personne/personne_form.html"
    def get_success_url(self):
        return reverse_lazy("details_personne", kwargs={"pk": self.object.id})
