import pytest
from django.test import TestCase

from todolist_rest.models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        print(Todo)
        git 
        Todo.make(content="eat dinner", done=False)
        Todo.objects.create(content="sleep", done=True)

    def test_Todo(self):
        eat = Todo.objects.get(id = 0)
        sleep = Todo.objects.get(id = 1)
        
    # def test_animals_can_speak(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')
