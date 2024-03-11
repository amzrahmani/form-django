from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from .forms import create_form


# Create your views here.
def home(request):
  all= Post.objects.all()
  return render(request, 'home.html',{'all':all})

def detail(request,post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'detail.html',{'post':post})

def delete(request,post_id):
   Post.objects.get(id=post_id).delete()
   messages.success(request,'cheraaaaaaa pak kardi',extra_tags='Warning')
   return redirect('home')

def create(request):
   if request.method == 'post':
    form = create_form(request.method)
    if form.is_valid():
     cd = form.cleaned_data
     Post.objects.create(title=cd['title'],body = cd['body'],date=cd['date'])
    messages.success(request,'afariiiiin','success')
    return redirect('home')

   else :
    form = create_form()
    return render(request, 'create.html',{'form':form})
