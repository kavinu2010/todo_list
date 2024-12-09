from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
from .forms import TaskForm
 


# Create your views here.
def home(request):
  tasks=Tasks.objects.all()
  return render(request, 'home.html', {'tasks':tasks})

def add_task(request):
  if request.method=='POST':
    form=TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    
  else :
    form=TaskForm()
  return render(request, 'add_tasks.html', {'form': form})
  

def task_detail(request, task_id):
   task = get_object_or_404(Tasks, id=task_id)
   return render(request, 'task_detail.html', {'task': task})
 