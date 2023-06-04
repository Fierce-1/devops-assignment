from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(browser, 20)
    browser.get('http://localhost:3000')
    browser.implicitly_wait(20)
    inputElement = browser.find_element(By.XPATH, "//*[@id='root']/div/header/div[2]/a/span[1]")
    inputElement.click()
    inputElement = browser.find_element(By.NAME, 'email')
    inputElement.send_keys('hes@gmail.com')
    inputElement = browser.find_element(By.NAME, 'password')
    inputElement.send_keys('12345')

    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button/span[1]').click()

    if browser.find_element(By.XPATH, '//*[@id="root"]/div/header/div[2]/div/button/span[1]'):
        print("test case 1: Passed User Login")

        data_input1 = browser.find_element(By.NAME, 'title')
        data_input1.send_keys('devops_assignment')

        data_input2 = browser.find_element(By.NAME, 'message')
        data_input2.send_keys('This is Devops Assignment 3')

        data_input3 = browser.find_element(By.NAME, 'tags')
        data_input3.send_keys('Jenkins, Docker, Dockerfile')

        data_input4 = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/form/button[1]/span[1]')
        data_input4.click()

        if WebDriverWait(browser, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[3]/div/h2'),
                                                 'devops_assignment')):
            print("test case 2: Passed Memory Created")
        else:
            print("test case 2: Failed Memory not Created")

        edit = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[3]/div/div[3]/button')
        edit.click()

        data_input_edit = browser.find_element(By.NAME, 'title')
        data_input_edit.send_keys('_3')

        data_input4 = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/form/button[1]/span[1]')
        data_input4.click()

        if WebDriverWait(browser, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[3]/div/h2'),
                                                 'devops_assignment_3')):
            print("test case 3: Passed Data in the Memory Updated")
        else:
            print("test case 3: Failed Data in the Memory not Updated")

        delete = browser.find_element(By.XPATH,
                                      '//*[@id="root"]/div/div/div/div[1]/div/div[3]/div/div[6]/button[2]/span[1]')
        delete.click()

        if WebDriverWait(browser, 10).until(EC.staleness_of(delete)):
            print("test case 4: Passed Memory Deleted")
        else:
            print("test case 4: Failed Memory not Deleted")

        logout = browser.find_element(By.XPATH, '//*[@id="root"]/div/header/div[2]/div/button/span[1]')
        logout.click()

        if browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h1'):
            print("test case 5: Passed User Logout")
        else:
            print("test case 5: Failed User Logout")

    browser.close()


except NoSuchElementException:
    print("test case 1: Failed User Login")
