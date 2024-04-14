from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "todo/todo.html")

def create(request):
    todo = request.GET.get("todo")
    return render(request, "todo/todo.html", {"todo":todo})

'''
def main(request):
    todos = TODO.objects.all()
    return render(request, "todo/todo.html", {"todo":todos})

def create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("todo_content")
        create_date = timezone.now()
        end_date = request.POST.get("end_date")
        todo = TODO.objects.create(title=title, content=content, end_date=end_date)
        return redirect('main')
        # return render(request, "todo/create.html")
    return render(request, "todo/todo.html")

def update(request, todo_id):
    todo = TODO.objects.get(pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('main')

def delete(request, todo_id):
    todo = TODO.objects.get(pk=todo_id)
    todo.delete()
    return redirect('main')
'''    

    