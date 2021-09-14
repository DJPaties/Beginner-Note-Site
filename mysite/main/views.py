from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import NoteTitle, Notedetails
from django.views import generic
from django.utils import timezone


# Create your views here.

class Homeview(generic.ListView):
    model = NoteTitle
    template_name = "main/home.html"

def Createnote(requests):

    if requests.method == "POST":
        if len(requests.POST.get("notesubject"))>0 and len(requests.POST.get("notedescription"))>0:
            print("pass")
            title = requests.POST.get("notesubject")
            desc = requests.POST.get("notedescription")
            create_note = NoteTitle.objects.create(note_text=title, pub_date=timezone.now())
            create_note.save()
            create_note.notedetails_set.create(details_text=desc)
            return HttpResponseRedirect(reverse("main:detailnote", args=(create_note.id,)))

        else:
            return render(requests, "main/create.html", {'errormessage':'Fill out the form'})
    return render(requests, "main/create.html", {})

class Detailnote(generic.DetailView):
    model = NoteTitle
    template_name = "main/detailnote.html"
    context_object_name = "notetitle"

class ListNotesView(generic.ListView):

    model = NoteTitle
    template_name = "main/listnotes.html"
    context_object_name = "notetitle"

    def get_queryset(self):
        return NoteTitle.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")

def deletenote(requests):
    notetitle = NoteTitle.objects.all()
    if requests.method == "POST":
        deletenote = requests.POST.get("noteid")
        if len(deletenote)>0 :
            if deletenote.isdigit():
               try:
                   del_note = NoteTitle.objects.get(id=deletenote)
               except (KeyError, NoteTitle.DoesNotExist):
                   return render(requests, "main/deletenote.html" , {'errormessage':'Note not found! wrong id number.', 'notetitle': notetitle})
               else:
                   del_note.delete()
                   return render(requests, "main/deletenote.html" , {'errormessage':'Note DELETED!', 'notetitle': notetitle})
            else:
                return render(requests, "main/deletenote.html" , {'errormessage':'Only numbers allowed', 'notetitle': notetitle})
        else:
            return render(requests, "main/deletenote.html" , {'errormessage':'Enter number id', 'notetitle': notetitle})

    else:
        pass

    return render(requests, "main/deletenote.html", {'notetitle': notetitle})
