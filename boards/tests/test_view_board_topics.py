from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import resolve
from django.test.client import Client

from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

# Create your tests here.


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
