from selenium import webdriver
import unittest

class AppTest(unittest.TestCase):
    def setUp(self):
        '''테스트 앞서 실행될 항목'''
        
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.implicitly_wait(10) # ajax call로 dom 재구성 하는경우에 사용, 최대 10초간 더 찾아보고 종료
        self.browser.get('http://localhost:8000')
    
    def test_startapp_0(self):
        '''테스트 메서드의 경우 작명시 반드시 "test_"의 형태로 할것'''

        self.assertIn('To-Do', self.browser.title)
 
    def tearDown(self):
        '''테스트 이후 실행될 항목'''
        self.browser.quit()
if __name__ == '__main__':
    unittest.main(warnings='ignore') # warnings='ignore'을 매개변수로 주면 실행시 에러나, 파일 로그를 무시한다.