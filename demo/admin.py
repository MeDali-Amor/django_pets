from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from demo.models.personne import Personne


@admin.register(Personne)
class PersonneAdmin(ImportExportModelAdmin):
    pass