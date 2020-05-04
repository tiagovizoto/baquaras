from django.contrib import admin
from .models import BackTestTryd


class BackTestTrydAdmin(admin.ModelAdmin):
    pass


admin.site.register(BackTestTryd, BackTestTrydAdmin)
