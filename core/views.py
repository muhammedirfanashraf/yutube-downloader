# from tkinter import filedialog
import easygui
from django.shortcuts import redirect, render
from pytube import YouTube

# Create your views here.

def path():
    path = easygui.filesavebox()
    return path


def home(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        print(link)
        global youtube
        youtube = YouTube(link)
        title = youtube.title
        thumbnail = youtube.thumbnail_url
        videos = youtube.streams.filter(progressive=True)
        context={'title': title, 'thumbnail': thumbnail, 'videos': videos}
        return render(request, 'index.html', context)
    return render(request, 'index.html')



def download(request, resolution):
    got_path = path()
    print('downloading')
    youtube.streams.filter(resolution=resolution).first().download(got_path)
    print('downloaded')
    return redirect('home')