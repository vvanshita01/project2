from django.shortcuts import render,redirect
from .models import book
from django.contrib import messages
# Create your views here.

def index(request):
    data=book.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        author=request.POST.get('author')
        isbn=request.POST.get('isbn')
        
        print(name,author,isbn)
        query=book(name=name,author=author,isbn=isbn)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        author=request.POST['author']
        isbn=request.POST['isbn']
       

        edit=book.objects.get(id=id)
        edit.name=name
        edit.author=author
        edit.isbn=isbn
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=book.objects.get(id=id) 
    context={"book":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=book.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")

def about(request):
    return render(request,"about.html")