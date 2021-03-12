from django.test import TestCase
from django.urls import reverse, resolve
from .models import Boards, Topics, Posts
from .views import homeView, boardFormView, topicFormView, topicsOfBoardView
# Create your tests here.

class HomeTest(TestCase):
    # def setUp(self):
    #     self.item = Boards.objects.create(name='Demo_Board', description='This board is created only for testing purpose...!')
    

    
    def setUp(self):
        self.brd = Boards.objects.create(name='demo_board', description='Test Board')


    def test_board_fields(self):
        item = Boards.objects.get(pk=self.brd.pk)
        self.assertEqual(item, self.brd)



    def test_home_view_status_code(self):
        url = reverse('app_boards:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_topicsOfBoardView_status_code(self):
        url = reverse('app_boards:board', kwargs={'board_id' : 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    

    def test_topicsOfBoardView_not_found_status_code(self):
        url = reverse('app_boards:board', kwargs={'board_id' : 10})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


    def test_topicsOfBoardView_url_resolve(self):
        view = resolve('/board/1/')
        self.assertEqual(view.func, topicsOfBoardView)
    