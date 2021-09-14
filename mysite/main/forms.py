from django.forms import ModelForm
from .models import NoteTitle, Notedetails

class Note_title(ModelForm):
    class Meta:
        model = NoteTitle
        exclude = ()

class Note_details(ModelForm):
    class Meta:
        model = Notedetails
        exclude = ()