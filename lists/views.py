from django.shortcuts import render


# Create your views here.
def home_page(request):
    # this takes the val from the test scirpt and insert it in the home
    # page
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
        })
