from django.contrib import admin
from models import *

admin.site.register(Maker)
admin.site.register(InstrumentImage)
admin.site.register(InstrumentType)
admin.site.register(InstrumentModel)


class InstrumentImageInline(admin.TabularInline):
    model = InstrumentImage

class InstrumentAdmin(admin.ModelAdmin):
    inlines = [
        InstrumentImageInline,
    ]

admin.site.register(Instrument, InstrumentAdmin)
