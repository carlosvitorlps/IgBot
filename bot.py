from selenium import webdriver
import time
import random
import getpass
from data_list import insta_users, post_id


class InstagramBot:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        # Needed to autometed Chrome
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get(f'{self.base_url}/accounts/login/')
        time.sleep(random.randint(2, 5))

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        # clicando no botão de login
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form\
            /div[4]/button').click()

        time.sleep(random.randint(2, 5))

    @staticmethod
    def type_as_person(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(2, 5)/30)

    def comment_on_post(self, id_publicacao):
        self.driver.get(f'{self.base_url}/{id_publicacao}/')

        time.sleep(random.randint(3, 5))

        # clicando na caixa de comentário

        text_box = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/section[3]/div/form/textarea'
        self.driver.find_element_by_xpath(text_box).click()

        time.sleep(random.randint(2, 4))

        tagging = insta_users

        while True:
            sample_3 = ''.join(random.sample(tagging, 3))
            where_type = self.driver.find_element_by_xpath(text_box)

            self.type_as_person((sample_3), where_type)
            time.sleep(random.randint(2, 4))

            post_button = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[3]/section[3]/div/form/button'
            self.driver.find_element_by_xpath(post_button).click()
            time.sleep(random.randint(100, 300))


if __name__ == '__main__':
    user = input('Username: ')
    password = getpass.getpass("Password: ")
    ig_bot = InstagramBot(user, password)
    post = post_id
    ig_bot.comment_on_post(post)
