from django.shortcuts import render, redirect

# In-memory task list
tasks = []

def todo_list(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            tasks.append(task)
        return redirect("todo")

    return render(request, "todo.html", {"tasks": tasks})


def delete_task(request, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("todo")


def clear_tasks(request):
    tasks.clear()
    return redirect("todo")

def edit_task(request, index):
    if request.method == "POST":
        new_task = request.POST.get("task")
        if new_task and 0 <= index < len(tasks):
            tasks[index] = new_task
        return redirect("todo")

    return render(request, "edit.html", {
        "task": tasks[index],
        "index": index
    })
