from django import forms
from .models import Folder
from mptt.forms import TreeNodeChoiceField


class NewFolderForm(forms.Form):
    name = forms.CharField(max_length=80)
    # parent = TreeNodeChoiceField(queryset=Folder.objects.all(), level_indicator='+--')
    parent = forms.ModelChoiceField(queryset=Folder.objects.all())

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']