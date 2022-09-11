from basepage import *



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