from django.shortcuts import render
from pytube import YouTube
# Create your views here.

def home(request):
    return render(request, "home.html")

def final(request):
    return render(request, "final.html")

def submit(request):
    url = request.GET['inp']
    url2 = url[17:]
    url3 = url[:11]
    obj = YouTube(url)
    streams = obj.streams.all()
    res = []
    for i in streams:
        res.append(i.resolution)
    res = list(dict.fromkeys(res))
    
    embed = url3+"tube.com/embed/"+url2  # slicing the main url and added "tube.com/embed/" to it to get the embed url
    return render(request, "list.html", {"url": url,"url2": url2, "embed": embed, "res": res})

def download(request, pixel):
    path = "C:/Downloads"
    pi = pixel[:4]
    val = pixel[4:]
    str = "www.youtube.com/watch?v=" + val
    obj = YouTube(str)
    obj.streams.filter(progressive=True,file_extension="mp4").get_by_resolution(pi).download(path)
    print("Video downloaded successfully")
    return render(request, "final.html")


