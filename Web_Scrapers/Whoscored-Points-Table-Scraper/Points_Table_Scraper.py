# Importing packages
from selenium.common.exceptions import NoSuchElementException
import csv
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import os.path

chrome_options = Options()
chrome_options.add_extension('Extensions\Adblock-Plus-free-ad-blocker_v3.8.0.crx')
chrome_options.add_argument('--disable-user-media-security')

driver = webdriver.Chrome(chrome_options=chrome_options)

league_urls = []

count_start = 0
count_end = 0


league_urls.append('https://www.whoscored.com/Regions/206/Tournaments/4/Spain-La-Liga')
league_urls.append('https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League')
league_urls.append('https://www.whoscored.com/Regions/108/Tournaments/5/Italy-Serie-A')
league_urls.append('https://www.whoscored.com/Regions/81/Tournaments/3/Germany-Bundesliga')
league_urls.append('https://www.whoscored.com/Regions/74/Tournaments/22/France-Ligue-1')
league_urls.append('https://www.whoscored.com/Regions/155/Tournaments/13/Netherlands-Eredivisie')


def bypass_cookie_request():
    try:
        driver.find_element_by_xpath('//*[@id="qcCmpButtons"]/button').click()
        # print('Cookie Confirmation bypassed')
        time.sleep(5)
    except NoSuchElementException:
        pass
        # print('Cookie Confirmation not found')


def find_league(url):
    league_country = str(url).lower()
    global count_start
    global count_end
    if league_country.find('netherlands') != -1 or league_country.find('france') != -1 or league_country.find('england') != -1 or league_country.find('germany') != -1:
        count_start = 2
        count_end = 11
    else:
        count_start = 1
        count_end = 10


def create_folder():
    try:
        os.mkdir('Datasets')
    except FileExistsError:
        pass


create_folder()


for x in range(0, len(league_urls)):

    driver.get(league_urls[x])
    time.sleep(5)

    bypass_cookie_request()

    find_league(league_urls[x])

    time.sleep(5)

    for y in range(count_start, count_end):

        driver.find_element_by_xpath('//*[@id="seasons"]/option[' + str(y) + ']').click()
        time.sleep(5)

        bypass_cookie_request()

        driver.execute_script("window.scrollTo(0, 1080)")

        table_id = str(driver.find_element_by_link_text('Standings').get_attribute('href')).split("#")[1]
        # print(table_id)

        stats = [[], [], [], [], [], [], [], [], [], []]

        stats[0].append('Rank')
        stats[1].append('Team')
        stats[2].append('Played')
        stats[3].append('Win')
        stats[4].append('Draw')
        stats[5].append('Loss')
        stats[6].append('Goals For')
        stats[7].append('Goals Against')
        stats[8].append('Goal Difference')
        stats[9].append('Points')

        row_count = 1

        try:
            while row_count > 0:
                stats[0].append(driver.find_element_by_xpath('//*[@id="'+ table_id +'-content"]/tr[' + str(row_count) + ']/td[1]/span').text)
                stats[1].append(driver.find_element_by_xpath('//*[@id="'+ table_id +'-content"]/tr[' + str(row_count) + ']/td[2]/a').text)
                for x in range(2, 10):
                    stats[x].append(driver.find_element_by_xpath('//*[@id="'+ table_id +'-content"]/tr[' + str(row_count) + ']/td[' + str(x+1) + ']').text)
                row_count += 1

        except NoSuchElementException:
            pass

        row = []

        league = Select(driver.find_element_by_id('tournaments')).first_selected_option.text.replace(' ', '')
        season = Select(driver.find_element_by_id('seasons')).first_selected_option.text.replace('/', '-')

        file_name = league + '-Points-Table-' + season

        with open(os.path.join('Datasets/', file_name + '.csv'), mode='w', encoding='UTF-8') as player_file:
            employee_writer = csv.writer(player_file)

            for c in range(0, len(stats[0])):
                for d in range(0, len(stats)):
                    row.append(stats[d][c])
                employee_writer.writerow(row)
                # print(row)
                row.clear()

            stats.clear()

        # df = pd.read_csv(file_name + '.csv', encoding='ISO-8859-1')
        # pd.options.display.width = 0
        # print(df)
        print('Datasets/' + file_name + '.csv Created.')








