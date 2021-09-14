from django.db import models
# Create your models here.
class NoteTitle(models.Model):
    note_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.note_text


class Notedetails(models.Model):
    notetitle = models.ForeignKey(NoteTitle, on_delete=models.CASCADE)
    details_text = models.CharField(max_length=700)

    def __str__(self):
        return self.details_text
