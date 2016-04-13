from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and acc tried to submit
        # an empty list item. She hits enter on teh empty input box

        # The haome page refershes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank item

        # She recives a similar warning on the list page

        # And she can correct it by filling some text it
        self.fail('write me!')
