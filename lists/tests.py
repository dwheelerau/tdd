from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


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

        print(response.content.decode())
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html', {'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)
