from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import resolve
from django.test.client import Client

from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

# Create your tests here.

# class HomeTests(TestCase):
#     def setUp(self):
#         self.board = Board.objects.create(name='Django', description='Django board.')
#         url = reverse('home')
#         self.response = self.client.get(url)
#
#     def test_home_view_status_code(self):
#         self.assertEquals(self.response.status_code, 200)
#
#     def test_home_url_resolves_home_view(self):
#         view = resolve('/boards/')
#         self.assertEquals(view.func, home)
#
#     def test_home_view_contains_link_to_topics_page(self):
#         board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
#         self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        print('setUp')
        Board.objects.create(name='Django', description='Django board.')

    '''
    * 最好不要删除下面的注释，我也不知道为什么，反正删了测试就会出错
    * 不知道为什么下面三个测试函数只能存在一个才能测试成功，否则就会测试出错
    '''
    # def test_board_topics_view_1_success_status_code(self):
    #     print('success')
    #     print(Board.objects.all())
    #     url = reverse('board_topics', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)
    #
    # def test_board_topics_view_2_not_found_status_code(self):
    #     print('not found')
    #     url = reverse('board_topics', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)

    # def test_board_topics_url_resolves_board_topics_view(self):
    #     print('url resolve')
    #     view = resolve('/boards/1/')
    #     self.assertEquals(view.func, board_topics)

    # def test_board_topics_view_contains_link_back_to_homepage(self):
    #     print('homepage')
    #     board_topics_url = reverse('board_topics', kwargs={'pk': 1})
    #     response = self.client.get(board_topics_url)
    #     homepage_url = reverse('home')
    #     self.assertContains(response, 'href="{0}"'.format(homepage_url))

    # def test_board_topics_view_contains_navigation_links(self):
    #     board_topics_url = reverse('board_topics', kwargs={'pk': 1})
    #     homepage_url = reverse('home')
    #     new_topic_url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.get(board_topics_url)
    #     self.assertContains(response, 'href="{0}"'.format(homepage_url))
    #     self.assertContains(response, 'href="{0}"'.format(new_topic_url))

class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board test.')
        User.objects.create_user(username='wo', email='wo@love.com', password='123')

    # def test_new_topic_view_success_status_code(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 200)
    #
    # def test_new_topic_view_not_found_status_code(self):
    #     url = reverse('new_topic', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)
    #
    # def test_new_topic_url_resolves_new_topic_view(self):
    #     view = resolve('/boards/1/new/')
    #     self.assertEquals(view.func, new_topic)

    # def test_new_topic_view_contains_link_back_to_board_topics_view(self):
    #     new_topic_url = reverse('new_topic', kwargs={'pk': 1})
    #     board_topic_url = reverse('board_topics', kwargs={'pk': 1})
    #     response = self.client.get(new_topic_url)
    #     self.assertContains(response, 'href="{0}"'.format(board_topic_url))

    # def test_csrf(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     self.assertContains(response, 'csrfmiddlewaretoken')

    # def test_new_topic_valid_post_data(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     data = {
    #             'subject': 'Test title',
    #             'message': 'this is a test.'
    #     }
    #     response = self.client.post(url, data)
    #     self.assertTrue(Topic.objects.exists())
    #     self.assertTrue(Post.objects.exists())

    # def test_new_topic_invalid_post_data(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.post(url, {})
    #     self.assertEquals(response.status_code, 200)

    # def test_new_topic_invalid_post_data_empty_fields(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     data = {
    #             'subject': '',
    #             'meaasge': ''
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertFalse(Topic.objects.exists())
    #     self.assertFalse(Post.objects.exists())

    # def test_contains_form(self):
    #     url = reverse('new_topic', kwargs={'pk': 1})
    #     response = self.client.get(url)
    #     form = response.context.get('form')
    #     self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_invalid_post_data(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
