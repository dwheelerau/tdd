from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # resolve is a django funct to resolve urls
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # http req obj when browswer ask for page
        request = HttpRequest()
        # pass it to homepage, that returns a response
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        # this just get the post that is name='item_text' in home.html
        # it is also just pretending to be user in this case
        # basically we are saying post a string in this form
        request.POST['item_text'] = 'A new list item'
        response = home_page(request)

        # this just makes sure that the response comes back

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html', {'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)

    def test_saving_and_retrieving_items(self):
        # classes are dbs, create hear see lists.models for class defn
        first_item = Item()
        # instances are cols ie text column
        first_item.text = 'The first (ever) list item'
        # create object at this row
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        # use .objects to acc all data, returns list like obj
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        # check to see if db object returns is recovered correctly
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
