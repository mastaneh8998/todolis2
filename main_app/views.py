from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
# Create your views here.
def logout_user(request):
    logout(request)
    return redirect("login")
def index(request):
    return render(request , "home.html")
@login_required
def home(request):
    if request.method == 'POST':
        task_name = request.POST.get("new-task")
        task_label = request.POST.get("task-label")
        
        if task_name and task_label:
            task = Task.objects.create(name=task_name, label=task_label, user=request.user)
            return redirect("home")

        # task = Task.objects.create(name=task_name, user=request.user , label=task_label)
        return redirect("home")

    tasks = Task.objects.filter(user=request.user, is_completed=False).order_by("-id")

    paginator = Paginator(tasks, 100)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"tasks": tasks, "page_obj": page_obj}
    return render(request, "Tasks.html", context)

def register(request):
    
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "signup.html", context)


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.name = request.POST.get(f"task_{pk}")
    task.label = request.POST.get(f"task_{pk}_label" )
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_task(request, pk):
    todo = get_object_or_404(Task, id=pk, user=request.user)
    todo.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complete_task(request, pk):    
    todo = get_object_or_404(Task, id=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))