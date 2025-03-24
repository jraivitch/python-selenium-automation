
#page: click / input text / find element

class Page:
    def click(self):
        print('clicking...')

    def find_element(self):
        print('finding...')

    def verify_text(self, text):
        print(f'verifying...{text}')


class MainPage(Page):
    def open_main(self):
        print('opening main page...')


class LoginPage(Page):
    def login(self):
        print('login')


login_page = LoginPage()
login_page.login()
login_page.click()
login_page.find_element()