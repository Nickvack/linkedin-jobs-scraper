import bs4
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# session = requests.Session()
#
# data = {'login': 'nvalencia1996@gmail.com', 'password': 'Nicolucas_1023'}
#
# req = session.post('https://www.linkedin.com/uas/login-submit', data=data)
#
# soup = bs4.BeautifulSoup(req.text, 'lxml')
#

# """
# {'JSESSIONID': 'ajax:6555787505932008259',
#     'li_rm': 'AQGbUFVPFVPycwAAAYJuYwt9hrN65op_RK9xg33f9cZnJAsgujZUrEsJlsbIkv9VIQsvS6uorYmJzqUz3QY696f0udK2ez52nB5VGT0RcjwZMcN2V_KIdM-V',
#     'bcookie': 'v=2&daca8ac6-934a-451a-8636-147b145c04a3',
#     'bscookie': 'v=1&20220805142240f580453a-eee6-4f7b-8664-d6454e252a1dAQHTjdhAKSAmDWkTl6y-qGRXcjxbs9M8',
#     'lidc': 'b=TGST04:s=T:r=T:a=T:p=T:g=2775:u=1:x=1:i=1659709361:t=1659795761:v=2:sig=AQGdonGej9_oCetj3MVDyu2wuzxkCkVy',}
# """
#
#
# #
# # soup
#
# client = requests.Session()
#
# HOMEPAGE_URL = 'https://www.linkedin.com'
# LOGIN_URL = 'https://www.linkedin.com/login-submit'
#
# html = client.get(HOMEPAGE_URL).content
# soup = bs4.BeautifulSoup(html, "lxml")
# csrf = soup.find(id="session_key")
#
# login_information = {
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                     'Chrome/99.0.4844.74 Safari/537.36 ',
#     'session_key': 'nvalencia1996@gmail.com',
#     'session_password': 'Nicolucas_1023',
#
# }
#
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/99.0.4844.74 Safari/537.36 '
#         }
#
# post = client.post(LOGIN_URL, data=login_information)
#
# # req = client.get('https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3201423217', headers=headers)
#
# client

path = 'C:/Users/Nickvack/Desktop/chromedriver.exe'
driver = webdriver.Chrome(path)

def linkedin_func():
    try:
        linked_home = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get(linked_home)

        driver.implicitly_wait(3)

        username = driver.find_element(By.ID, 'username')

        password = driver.find_element(By.ID, 'password')

        button = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')

        driver.implicitly_wait(3)

        username.send_keys('nickvack783@gmail.com')

        password.send_keys('Azul_1023')

        button.click()

        driver.implicitly_wait(3)

        jobs = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[3]/a')

        jobs.click()

        driver.implicitly_wait(3)

        driver.get('https://www.linkedin.com/jobs/search/')

        driver.implicitly_wait(3)

        input_search_criteria = input('what do you want to search for? ').replace(' ', '%20')

        location = input('where do you want to search').replace(' ', '&')

        scrape_url = driver.current_url + '&keywords=' + input_search_criteria + '&location=' + location + '&start=25'

        driver.get(scrape_url)

        driver.implicitly_wait(3)

        # form_with_urls = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list')
        #
        # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", form_with_urls)
        #
        # driver.implicitly_wait(3)

        time.sleep(3)

        form_with_urls = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list')

        driver.execute_script("var el = document.getElementsByClassName('jobs-search-results-list')[0]; el.scroll(0, "
                              "900)")

        driver.implicitly_wait(3)

        time.sleep(1)

        driver.execute_script("var el = document.getElementsByClassName('jobs-search-results-list')[0]; el.scroll(0, "
                              "1800)")

        driver.implicitly_wait(3)

        time.sleep(1)

        driver.execute_script("var el = document.getElementsByClassName('jobs-search-results-list')[0]; el.scroll(0, "
                              "2200)")

        driver.implicitly_wait(3)

        time.sleep(1)

        driver.execute_script(
            "var el = document.getElementsByClassName('jobs-search-results-list')[0]; el.scroll(0, el.scrollHeight)")

        driver.implicitly_wait(3)

        time.sleep(2)

        driver.execute_script(
            "var el = document.getElementsByClassName('jobs-search-results-list')[0]; el.scroll(0, el.scrollHeight)")

        driver.implicitly_wait(3)

        time.sleep(2)

        list_bad_urls = driver.find_elements(By.CLASS_NAME, 'job-card-container__link')

        driver.implicitly_wait(3)

        list_of_urls = [x.get_attribute('href') for x in list_bad_urls if 'job-card-list__title' in x.get_attribute('class')]

        for url in list_of_urls:

            driver.get(url.get_attribute('href'))

            driver.implicitly_wait(3)

            driver












    except Exception as e:
        print(e)


linkedin_func()









