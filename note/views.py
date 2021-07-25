from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from note.models import notes
from note.forms import NotesForm

 

@login_required(login_url='login')
def dashBoard(request):
    if request.method == 'GET':
        tasks = notes.objects.filter(user=request.user)
        context = {"tasks": tasks}
        return render(request, 'dashboard.html', context=context)


@login_required(login_url='login')
def createNotes(request):

    if request.method == 'GET':
        context = {'createForm': NotesForm}
        return render(request, 'create.html', context=context)

    if request.method == 'POST':
        data = {}
        data['user'] = request.user
        data['title'] = request.POST.get('title')
        data['description'] = request.POST.get('description')
        form = NotesForm(data)
        if form.is_valid():
            form.save()
        return redirect('dashboard')


@login_required(login_url='login')
def updateNotes(request, pk):
    note = notes.objects.get(id=pk)

    if request.method == 'GET':    
        form = NotesForm(instance=note)
        context = {'form': form, 'pk': pk}
        return render(request, 'update.html', context=context)

    elif request.method == 'POST':
        data = {}
        data['user'] = request.user
        data['title'] = request.POST.get('title')
        data['description'] = request.POST.get('description')
        data['finished'] = request.POST.get('finished')
        form = NotesForm(data, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard')


@login_required(login_url='login')
def deleteTask(request, pk):
    note = notes.objects.get(id=pk)
    note.delete()
    return redirect('dashboard')

