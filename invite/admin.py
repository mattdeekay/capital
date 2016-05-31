from django.contrib import admin

from .models import EmailAccess, AccessCode

admin.site.register(EmailAccess)
admin.site.register(AccessCode)
#admin.site.register(NdaCheckBox)
# Register your models here.
