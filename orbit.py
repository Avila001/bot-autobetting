from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bot import game_name_orbit

game_name = game_name_orbit[0]
game_outcome = game_name_orbit[1]
need_sum = 7


# Initialize Chrome WebDriver
chrome_options = Options()
driver = webdriver.Chrome(executable_path="C:\Python39\chromedriver.exe", options=chrome_options)

driver.maximize_window()



driver.get("https://www.orbitexch.com/customer/inplay/highlights/1")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="biab_login-block"]/div/form/fieldset/div[1]/div[3]/span'))
    )
except:
    print('some error happen !!')

username = driver.find_element('name', 'username')
password = driver.find_element('name', 'password')
login = driver.find_element('xpath', '//*[@id="biab_login-block"]/div/form/fieldset/div[1]/div[3]/span')

username.send_keys("dzute20gex")
password.send_keys("!$Dtcnthjc05")
login.click()

#ждем Всплывающее окно Terms - жмем OK
try:
    button_OK = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="biab_modal"]/div/div/div[1]/div/div[2]/div[7]/div'))
    )
    button_OK = driver.find_element('xpath', '//*[@id="biab_modal"]/div/div/div[1]/div/div[2]/div[7]/div').click()
except:
    print('some error happen !!')

    


time.sleep(2.5)

search_game = driver.find_element('name', 'search')

for i in game_name:
    search_game.send_keys(i)
    time.sleep(0.05)

# Переходим на страницу матча
time.sleep(2.5)
href_game = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[2]/div/div[5]/div[1]/div[2]/div/div/div[1]/a')
if href_game.text == game_name:
    href_game.click()

#теперь пишем хозяева гости и за кого ставим
def pick_side_and_back_or_lay():
    '''Выбираем команду и выбор набора: back or lay'''
    ht_odd = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[4]/div/div/div/span[1]')
    at_odd = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[4]/div/div/div/span[1]')
    if game_outcome == 'Хозяева':
        # Сравниваем кэфы за хозяев и за гостей
        if float(ht_odd.text) <= float(at_odd.text):
            # Back за хозяев (Man Utd v Brighton) Back Man Utd
            odd1 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[4]')
            odd2 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[3]')
            odd3 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[2]')
            odd1_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[4]/div/div/div/span[2]').text)
            odd2_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[3]/div/div[1]/div/span[2]').text)
            odd3_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[2]/div/div/div/span[2]').text)
        if float(ht_odd.text) > float(at_odd.text):
            # Lay гостей (West Ham v Man City) Lay Man City
            odd1 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[5]')
            odd2 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[6]')
            odd3 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[7]')
            odd1_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[5]/div/div/div/span[2]').text)
            odd2_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[6]/div/div/div/span[2]').text)
            odd3_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[7]/div/div/div/span[2]').text)
    if game_outcome == 'Гости':
        if float(ht_odd.text) <= float(at_odd.text):
            # lay хозяев (Man Utd v Brighton) Lay Man Utd
            odd1 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[5]')
            odd2 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[6]')
            odd3 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[7]')
            odd1_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[5]/div/div/div/span[2]').text)
            odd2_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[6]/div/div/div/span[2]').text)
            odd3_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[7]/div/div/div/span[2]').text)
        if float(ht_odd.text) > float(at_odd.text):       
            # Back гостей (West Ham v Man City) Back Man City
            odd1 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[4]')   
            odd2 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[3]')
            odd3 = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[2]')
            odd1_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[4]/div/div/div/span[2]').text)
            odd2_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[3]/div/div[1]/div/span[2]').text)
            odd3_amount = float(driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[2]/div/div/div/span[2]').text)
    list_odds_amount = [[odd1, odd1_amount], [odd2, odd2_amount], [odd3, odd3_amount]]
    return list_odds_amount

def place_bet():
    '''Делаем ставку. Продумать ограничение по времени и возможное дублирование ставки (от разных капперов или 2 ставки (возможна обратная) от одного.'''
    list_odds_amounts = pick_side_and_back_or_lay()
    odd1 = list_odds_amounts[0][0]
    odd2 = list_odds_amounts[1][0]
    odd3 = list_odds_amounts[2][0]
    odd1_amount = list_odds_amounts[0][1]
    odd2_amount = list_odds_amounts[1][1]
    odd3_amount = list_odds_amounts[2][1]
    
    if odd1_amount >= need_sum:
        desired_odd = odd1
    elif odd1_amount + odd2_amount >= need_sum:
        desired_odd = odd2
    else:
        desired_odd = odd3
    desired_odd.click()
    # stake_input = driver.find_element('xpath', '//*[@id="biab_placeBets"]/div/form/table[1]/tbody/tr/td/table/tbody/tr[1]/td[3]/input').send_keys(need_sum)
    try:
        wait_stake_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="biab_placeBets"]/div/form/table[1]/tbody/tr/td/table/tbody/tr[1]/td[3]/input'))
        )
        stake_input = driver.find_element('xpath', '//*[@id="biab_placeBets"]/div/form/table[1]/tbody/tr/td/table/tbody/tr[1]/td[3]/input').send_keys(need_sum)
        time.sleep(0.5)
        button_place_bets = driver.find_element('xpath', '//*[@id="biab_placeBetsBtn"]').click()
    except:
        print('Окно для ввода ставки не открылось.')

#ищем элемент первый кэф    
try:
    first_odd = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[4]/div/div/div/span[2]'))
    )
    # button_OK = driver.find_element('xpath', '//*[@id="biab_content"]/div/div[3]/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/table/tbody/tr/td[4]/div/div/div/span[2]').click()
except:
    print('some error happen !!')

place_bet()

    
time.sleep(5)


# '//*[@id="biab_login-block"]/div/form/fieldset/div[1]/div[1]/input'
# '//*[@id="biab_login-block"]/div/form/fieldset/div[1]/div[2]/input'

# time.sleep(5)
# login_form = driver.find_element('xpath', '//*[@id="biab_headerAccountNavigation"]/div[2]/button')
# soccer_form = driver.find_element('xpath', '//*[@id="biab_header_navigatinItems"]/div/div[1]/div/div/ul/li[4]/a')

driver.quit()
