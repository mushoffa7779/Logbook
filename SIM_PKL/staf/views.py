from django.shortcuts import render,redirect
from . import models, forms


def mitra(req):
    mitra = models.Mitra.objects.all()
    return render(req, 'index.html',{
        'data': mitra,
    })


def new(req):
    form_input = forms.MitraForm()
    if req.POST:
        form_input = forms.MitraForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/staf/mitra/')
    return render(req, 'new.html',{
        'form' : form_input,
    })

def detail(req, id):
    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'detail.html', {
        'data': mitra,
    })

def delete(req, id):
    models.Mitra.objects.filter(pk=id).delete()
    return redirect('/staf/mitra/')

def update(req, id):
    if req.POST:
        mitra = models.Mitra.objects.filter(pk=id).update(nama=req.POST['nama'], alamat=req.POST['alamat'], status=req.POST['status'])
        return redirect('/staf/mitra/')

    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'update.html', {
        'data': mitra,
    })