from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("home/", views.Homeview.as_view(), name="home"),
    path("create/", views.Createnote, name="create"),
    path("listnotes/", views.ListNotesView.as_view(), name="listnotes"),
    path("note/<int:pk>/", views.Detailnote.as_view(), name="detailnote"),
    path("deletenote/", views.deletenote, name="deletenote")
]