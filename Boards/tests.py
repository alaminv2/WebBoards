from django.test import TestCase
from django.urls import reverse, resolve
from .models import Boards, Topics, Posts
from .views import homeView, boardFormView, topicFormView, boardTopicsView, newTopicView
from .forms import TopicForm
from django.contrib.auth.models import User

# Create your tests here.


class TestAllViewsStatusCode(TestCase):
    def setUp(self):
        self.board = Boards.objects.create(name='demo_board', description='Test Board')

    def test_home_view_status_code(self):
        response = self.client.get(reverse('app_boards:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_board_topics_view_status_code(self):
        response = self.client.get(reverse('app_boards:board_topics', kwargs={'board_id' : self.board.pk}))
        self.assertEqual(response.status_code, 200)
    
    def test_create_board_view_status_code(self):
        response = self.client.get(reverse('app_boards:board_form'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_topic_view_status_code(self):
        response = self.client.get(reverse('app_boards:topic_form', kwargs={'board_id' : self.board.pk}))
        self.assertEqual(response.status_code, 200)

        

class HomeTest(TestCase):
    def setUp(self):
        self.board = Boards.objects.create(name='demo_board', description='Test Board')
        url = reverse('app_boards:home')
        self.response = self.client.get(url)


    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)



    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, homeView)

    
    def test_home_view_contains_links_to_boardtopics_page(self):
        board_topics_url = reverse('app_boards:board_topics', kwargs={'board_id': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('app_boards:board_topics', kwargs={'board_id': self.board.pk})
        response = self.client.get(board_topics_url)
        home_url = reverse('app_boards:home')
        self.assertContains(response, 'href="{0}"'.format(home_url))



class BoardTopicsTest(TestCase):
    def setUp(self):
        self.board = Boards.objects.create(name='for testing board_topics', description='Testing Purpose')
    
    def test_boardtopics_contains_navigation_links(self):
        boardtopics_url = reverse('app_boards:board_topics', kwargs={'board_id': self.board.pk})
        home_url = reverse('app_boards:home')
        newtopic_url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        response = self.client.get(boardtopics_url)

        self.assertContains(response, 'href="{0}"'.format(home_url))
        self.assertContains(response, 'href="{0}"'.format(newtopic_url))


class NewTopicTest(TestCase):
    def setUp(self):
        self.board = Boards.objects.create(name="demo_board", description="This is a board")
        User.objects.create(username="alamin", email="alamin@gmail.com", password="alamin")


    def test_new_topic_status_code(self):
        response = self.client.get(reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk}))
        self.assertEqual(response.status_code, 200)
    
    def test_new_topic_not_found_status_code(self):
        response = self.client.get(reverse('app_boards:new_topic', kwargs={'board_id': 40}))
        self.assertEqual(response.status_code, 404)
    
    def test_new_topic_url_resolves_new_topi_view(self):
        view = resolve('/new_topic/<self.board.pk>/')
        self.assertEquals(view.func, newTopicView)
    
    def test_new_topic_contains_navigation_link(self):
        url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        response = self.client.get(url)
        target_url = reverse('app_boards:board_topics', kwargs={'board_id': self.board.pk})
        self.assertContains(response, 'href="{0}"'.format(target_url))
    
    def test_csrf(self):
        url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')
    
    def test_new_topic_valid_post_data(self):
        url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        data = {
            'subject' : 'posted from test file',
            'message' : 'This is for only testing purpose'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topics.objects.exists())
        self.assertTrue(Posts.objects.exists())

# Thsi 2 functions are Not applicable for the manual form
    def test_new_topic_invalid_post_data(self):
        url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        data = {}
        response = self.client.post(url, data)
        form = response.context.get('form')
        self.assertTrue(form.errors)
        self.assertEqual(response.status_code, 200)    
    
    def test_new_topic_invalid_post_data_empty_fields(self):
        url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        data = {
            'subject' : '',
            'message' : ''
        }
        response = self.client.post(url, data)
        form = response.context.get('form')
        self.assertTrue(form.errors)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Topics.objects.exists())
        self.assertFalse(Posts.objects.exists())
    
    def test_contains_forms(self):
        url = reverse('app_boards:new_topic', kwargs={'board_id': self.board.pk})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, TopicForm)
        # print('space = ', int(' '))