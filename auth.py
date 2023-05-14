class TestLogin:
    def setup_method_signup(self):
        options = Options()
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://qauto2.forstudy.space/api/auth/signup")
        self.sign_up_page = SignUpPage(self.driver)


    def setup_method_login(self):
        self.login_page.login('admin@yourstore.com', 'admin')

