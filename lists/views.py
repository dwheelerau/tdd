from django.shortcuts import redirect, render
from lists.models import Item


# Create your views here.
def home_page(request):
    # this takes the val from the test scirpt and insert it in the home
    # page
    # save object in database, tests.py recovers
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
