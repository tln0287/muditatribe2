from django.shortcuts import render

# Create your views here.
from counsellor.encryption_util import decrypt
from music.models import AddMusic


def music_details(request,id):
    id = decrypt(id)
    data = AddMusic.objects.get(id=id)
    adata = AddMusic.objects.all()
    return render(request,'web/music_d.html',{'data':data,'adata':adata})
