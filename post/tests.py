from django.test import TestCase
from django.urls import resolve
from post.views import homepage_view
from django.http import HttpRequest

class HomepageTest(TestCase):
    def test_root_url_match_to_homepage_view(self):
        '''루트 URL과 매칭된 fbv 를 비교하는 단위테스트 메서드'''
        root_url_view = resolve('/') # 해당 메서드는 매개변수로 받는 URI와 매핑된 함수 반환
        self.assertEqual(root_url_view.func, homepage_view)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = homepage_view(request)
        self.assertTrue(response.content.startswith(b'<html>')) #content 는 byte type이기에 b"str" 로 비교
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))