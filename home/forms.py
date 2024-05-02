from django import forms
from .models import FavoriteKit

class FavoriteKitForm(forms.ModelForm):
    class Meta:
        model = FavoriteKit
        fields = []

        