from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    Task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    # Check if there already exists a "tasks" key in our session
    if "Tasks" not in request.session:
        request.session["Tasks"] = [] # If not, create a new list
    return render(request, "Tasks/index.html", {
        "Tasks": request.session["Tasks"]
    })

# Add a new task:
def add(request):
    if request.method == "POST":      # Check if method is POST
        form = NewTaskForm(request.POST)     # Take in the data the user submitted and save it as form
        if form.is_valid():      # Check if form data is valid (server-side)
            Task = form.cleaned_data["Task"]      # Isolate the task from the 'cleaned' version of form data
            request.session["Tasks"] += [Task]    # Add the new task to our list of tasks
            # ( *** Tasks.append(Task) ***)       # Add the new task to our list of tasks
            return HttpResponseRedirect(reverse("Tasks:index"))    # Redirect user to list of tasks
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "Tasks/add.html", {
                "form": form
            })
    
    return render(request, "Tasks/add.html", {
        "form": NewTaskForm()
    })