from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Folder
from .forms import NewFolderForm

def get_folders_view(request):
    my_folders = Folder.objects.all()
    return render(request, 'folders.html', {"folders": my_folders})

def add_folder_view(request):
    if request.method == "POST":
        form = NewFolderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Folder.objects.create(
                name=data.get('name'),
                parent=data.get('parent')
                )
            return redirect('homepage')

    form = NewFolderForm()
    return render(request, 'new_folder.html', {"form": form})
    
