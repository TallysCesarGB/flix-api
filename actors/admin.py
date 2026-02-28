# admin.py
from django import forms
from django.contrib import admin
from .models import Actor



class ActorAdminForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        widgets = {
            'nationality': forms.TextInput(attrs={
                'id': 'nationality-input',
                'autocomplete': 'off',
            })
        }

    class Media:
        js = ('admin/js/nationality_autocomplete.js',)

class ActorAdmin(admin.ModelAdmin):
    form = ActorAdminForm
    list_display = ('name', 'birth_date', 'nationality',)

admin.site.register(Actor, ActorAdmin)