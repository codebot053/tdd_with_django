from django.test import TestCase
from django.urls import resolve
from post.views import homepage_view

class HomepageTest(TestCase):
    def test_root_url_match_to_homepage_view(self):
        '''루트 URL과 매칭된 fbv 를 비교하는 단위테스트 메서드'''
        root_url_view = resolve('/') # 해당 메서드는 매개변수로 받는 URI와 매핑된 함수 반환
        self.assertEqual(root_url_view, homepage_view)
