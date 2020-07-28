from selenium import webdriver
import time
import random
import getpass


class InstagramBot:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get(f'{self.base_url}/accounts/login/')

        time.sleep(random.randint(2, 5))

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        # clicando na no botão de login
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form\
            /div[4]/button').click()

        time.sleep(random.randint(2, 5))

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(2, 5)/30)

    def comentar_publicacao(self, id_publicacao):
        self.driver.get(f'{self.base_url}/{id_publicacao}/')

        time.sleep(random.randint(3, 5))

        # clicando na caixa de comentário

        caixa_comentario = '//*[@id="react-root"]/section/main/div/div[1]/article\
            /div[3]/section[3]/div/form/textarea'
        self.driver.find_element_by_xpath(caixa_comentario).click()

        time.sleep(random.randint(2, 4))

        marcacao = ["@yanneareas  @liviagomesreis  @luluzinha_avila",
                    "@yanneareas  @liviagomesreis  @animacaoleticia",
                    "@yanneareas  @liviagomesreis  @darcielyf",
                    "@yanneareas  @liviagomesreis  @thaisgetti",
                    "@yanneareas  @luluzinha_avila  @animacaoleticia",
                    "@yanneareas  @luluzinha_avila  @darcielyf",
                    "@yanneareas  @luluzinha_avila  @thaisgetti",
                    "@yanneareas  @animacaoleticia  @darcielyf",
                    "@yanneareas  @animacaoleticia  @thaisgetti",
                    "@yanneareas  @darcielyf  @thaisgetti",
                    "@liviagomesreis  @luluzinha_avila  @animacaoleticia",
                    "@liviagomesreis  @luluzinha_avila  @darcielyf",
                    "@liviagomesreis  @luluzinha_avila  @thaisgetti",
                    "@liviagomesreis  @animacaoleticia  @darcielyf",
                    "@liviagomesreis  @animacaoleticia  @thaisgetti",
                    "@liviagomesreis  @darcielyf  @thaisgetti",
                    "@luluzinha_avila  @animacaoleticia  @darcielyf",
                    "@luluzinha_avila  @animacaoleticia  @thaisgetti",
                    "@luluzinha_avila  @darcielyf  @thaisgetti",
                    "mariaclaramenezes__ @darcielyf  @thaisgetti",
                    "mariaclaramenezes__ @martaarteira56  @thaisgetti",
                    "@ribeirocosta90  @darcielyf  @alessandracdancer"]

        while True:
            self.digite_como_uma_pessoa(random.choice(
                marcacao), self.driver.find_element_by_xpath(caixa_comentario))
            time.sleep(random.randint(2, 4))

            publicar_button = '//*[@id="react-root"]/section/main/div/div[1]/article\
                /div[3]/section[3]/div/form/button'
            self.driver.find_element_by_xpath(publicar_button).click()
            time.sleep(random.randint(20, 300))


if __name__ == '__main__':
    # não é boa prática. olhar o conceito do .gitignore

    user = input('Usuário: ')
    senha = getpass.getpass("Enter your password: ")
    ig_bot = InstagramBot(user, senha)
    ig_bot.comentar_publicacao('p/CDBnmPdp7qg')  # endereço da publicação
