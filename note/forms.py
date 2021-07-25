from django import forms
from note.models import notes


class NotesForm(forms.ModelForm):

    class Meta:
        model = notes
        fields = ['user', 'title', 'description', 'finished']