from selenium import webdriver
import unittest

class TodoAppTest(unittest.TestCase):
    # 할일 목록(To-do) 사이트 사용자 스토리
    def setUp(self):
        '''테스트 앞서 실행될 항목'''
        # 성우는 새로운 할일 정리 사이트를 발견하고 접속해보았다.
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.implicitly_wait(10) # ajax call로 dom 재구성 하는경우에 사용, 최대 10초간 더 찾아보고 종료
        self.browser.get('http://localhost:8000')
    
    def test_startapp_0(self):
        '''테스트 메서드의 경우 작명시 반드시 "test_"의 형태로 할것'''
        
        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        # assert 보다 assertIn 메서드 사용시 좀더 명시적이고 친절한 Error 메세지를 확인할 수 있다.
        self.assertIn('To-do', self.browser.title)
        # 성우는 한번 할일을 추가해보기로 했다.
        # "스터디 준비하기"라고 텍스트 상자에 입력한다. (성우는 오늘도 스터디에 고통받는다)

        # 엔터키를 치면 페이지가 갱신되고 할일 목록에 "1. 스터디 준비하기" 아이템이 추가된다.

        # 그 아래 추가로 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
        # 다시 "스터디 자료 정리하기"라고 입력한다.

        # 페이지가 다시 갱신되고, 두 개 아이템이 목록에 보인다.
        # 성우는 사이트가 입력한 목록을 저장하고 있는지 궁금해졌다.
        # 사이트는 성우를 위한 특정 URL을 생성해준다.
        # 이때 URL에 대한 설명도 함께 제공된다.

        # 해당 URL에 접속하면 성우가 만든 할일 목록이 그대로 있는 것을 확인할 수 있다.

    def test_startapp_1(self):
        '''2번째 테스트는 1번째 테스트가 실행되고난 후 다시 브라우저를 열어 실행한다.'''
        self.assertEqual('The install worked successfully! Congratulations!', self.browser.title)
        
        
    def tearDown(self):
        '''테스트 이후 실행될 항목'''
        # 만족하고 웹사이트를 끈다.
        self.browser.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore') # warnings='ignore'을 매개변수로 주면 실행시 에러나, 파일 로그를 무시한다.