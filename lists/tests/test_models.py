from django.test import TestCase
# this inports the database
from lists.models import Item, List


class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        # classes are dbs, create hear see lists.models for class defn
        list_ = List()
        list_.save()

        first_item = Item()
        # instances are cols ie text column
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        # create object at this row
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_items = List.objects.first()
        self.assertEqual(saved_items, list_)

        # use .objects to acc all data, returns list like obj
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        # check to see if db object returns is recovered correctly
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)
