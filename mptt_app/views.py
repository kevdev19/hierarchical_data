from django.shortcuts import render

from .models import Folder

def get_folders_view(request):
    my_folders = Folder.objects.all()
    return render(request, 'folders.html', {"folders": my_folders})
