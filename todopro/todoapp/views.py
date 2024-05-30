from django.shortcuts import render,redirect,get_object_or_404
from . models import todoitem
# Create your views here.
def index(request):
        if request.POST:
          title=request.POST.get('title')
          todo_obj=todoitem(title=title)      
          todo_obj.save()
          return redirect(index)    
        else:
          todo_obj=todoitem.objects.all()
          return render(request,'index.html',{'todos':todo_obj})   
    
def delete_g(request,pk):
    todo_obj=todoitem.objects.get(pk=pk)
    todo_obj.delete()
    return redirect(index)

def edit_g(request, pk ):
     if request.method =="POST":
          title=request.POST.get('title')
          todoitem.objects.filter(pk=pk).update(title=title)
          return redirect('index')
     else:                    
          todoobj=todoitem.objects.all()
          data=todoitem.objects.get(pk=pk)
          return render(request,'index.html',{'data':data,'todos':todoobj})

          

    