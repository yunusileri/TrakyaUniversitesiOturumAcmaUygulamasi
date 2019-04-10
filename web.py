from selenium import webdriver
import time, datetime
import requests

user_name = ''
user_pwd = ''


def user():
    global user_pwd, user_name
    try:
        file = open('user.txt', 'r')
        a = file.read()
        user_name, user_pwd = a.split('\n')
        print(user_name, user_pwd)
    except IOError:
        user_name = input('Kullanıcı adinizi giriniz.\n')
        user_pwd = input('Şifrenizi giriniz.\n')
        f = open('user.txt', 'a')
        f.write(f'{user_name}\n{user_pwd}')
        f.close()


def Baglan():
    global user_name, user_pwd
    user()
    driver_path = r'/Users/mac16/Desktop/chromedriver'
    browser = webdriver.Chrome(executable_path=driver_path)
    time.sleep(2)
    browser.get('https://www.haberturk.com')
    time.sleep(2)

    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')

    username.send_keys(user_name)
    password.send_keys(user_pwd)
    time.sleep(1)

    giris_button = browser.find_element_by_xpath("//input[@type='submit']")
    giris_button.click()
    time.sleep(1)
    file = open('Log.txt', 'a')
    file.write(f'Baglanti Acildi {datetime.datetime.now()}\n\n')
    print(f'Baglanti Acildi {datetime.datetime.now()}\n\n')

    browser.close()


def Baglanti_Kontrol():
    MyUrl = 'https://github.com/'
    try:
        req = requests.get(MyUrl)
        file = open('Log.txt', 'a')
        file.write(f'Baglanti Acik {datetime.datetime.now()}\n')
        print(f'Baglanti Acik {datetime.datetime.now()}\n')
    except:
        file = open('Log.txt', 'a')
        file.write(f'Baglanti Yok {datetime.datetime.now()}\n')
        print(f'Baglantı Yok {datetime.datetime.now()}\n')
        return Baglan()


while True:
    Baglanti_Kontrol()
    time.sleep(300)
