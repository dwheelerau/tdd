from django.shortcuts import redirect, render
from lists.models import Item, List
from lists.forms import ItemForm


# Create your views here.
def home_page(request):
    # this takes the val from the test scirpt and insert it in the home
    # page
    # save object in database, tests.py recovers
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    # get the database entry for the list_id entered in the url
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {
        'list': list_, "form": form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
