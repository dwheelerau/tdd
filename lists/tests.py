from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# this inports the database
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


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        # Create two items in db
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):

        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

        self.assertRedirects(
            response, '/lists/the-only-list-in-the-world/')
