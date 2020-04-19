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


for x in range(0, len(league_urls)):

    create_folder()

    driver.get(league_urls[x])
    time.sleep(5)

    bypass_cookie_request()

    find_league(league_urls[x])

    time.sleep(5)

    for y in range(count_start, count_end):

        driver.find_element_by_xpath('//*[@id="seasons"]/option[' + str(y) + ']').click()
        driver.find_element_by_xpath('//*[@id="sub-navigation"]/ul/li[4]/a').click()
        time.sleep(5)

        bypass_cookie_request()

        driver.execute_script("window.scrollTo(0, 1080)")

        for z in range(1, 5):

            driver.find_element_by_xpath('//*[@id="stage-top-player-stats-options"]/li[' + str(z) + ']/a').click()

            time.sleep(5)

            driver.find_element_by_link_text('All players').click()

            time.sleep(5)

            stats = None

            tb_id = None

            paging_id = None

            category = None

            if z == 1 or z == 2:
                stats = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
            if z == 3:
                stats = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
            if z == 4:
                stats = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]

            stats[0].append('Name')
            stats[1].append('Team')
            stats[2].append('Age')
            stats[3].append('Position')
            stats[4].append('Apps')
            stats[5].append('Minutes')

            if z == 1:
                stats[6].append('Total Goals')
                stats[7].append('Total Assists')
                stats[8].append('Yellow cards')
                stats[9].append('Red cards')
                stats[10].append('Shots per game')
                stats[11].append('Pass success percentage')
                stats[12].append('Aerials won per game')
                stats[13].append('Man of the match')
                stats[14].append('Rating')
                category = 'Summary'
                tb_id = '//*[@id="statistics-table-summary"]'
                paging_id = '//*[@id="statistics-paging-summary"]'

            elif z == 2:
                stats[6].append('Tackles per game')
                stats[7].append('Interceptions per game')
                stats[8].append('Fouls per game')
                stats[9].append('Offsides per game')
                stats[10].append('Clearances per game')
                stats[11].append('Dribbled past per game')
                stats[12].append('Outfield blocks per game')
                stats[13].append('Own goals')
                stats[14].append('Rating')
                category = 'Defensive'
                tb_id = '//*[@id="statistics-table-defensive"]'
                paging_id = '//*[@id="statistics-paging-defensive"]'
            elif z == 3:
                stats[6].append('Total goals')
                stats[7].append('Total Assists')
                stats[8].append('Shots per game')
                stats[9].append('Key passes per game')
                stats[10].append('Dribbles per game')
                stats[11].append('Fouled per game')
                stats[12].append('Offsides per game')
                stats[13].append('Dispossessed per game')
                stats[14].append('Bad control per game')
                stats[15].append('Rating')
                category = 'Offensive'
                tb_id = '//*[@id="statistics-table-offensive"]'
                paging_id = '//*[@id="statistics-paging-offensive"]'
            elif z == 4:
                stats[6].append('Total Assists')
                stats[7].append('Key passes per game')
                stats[8].append('Passes per game')
                stats[9].append('Pass success percentage')
                stats[10].append('Crosses per game')
                stats[11].append('Long balls per game')
                stats[12].append('Through balls per game')
                stats[13].append('Rating')
                category = 'Passing'
                tb_id = '//*[@id="statistics-table-passing"]'
                paging_id = '//*[@id="statistics-paging-passing"]'

            hasNextPage = True

            while hasNextPage:
                try:
                    for a in range(1, 11):
                        stats[0].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[3]/a[1]').text)
                        stats[1].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(
                                a) + ']/td[3]/a[2]/span').text.replace(',', ''))
                        stats[2].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[3]/span[1]').text)
                        stats[3].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(
                                a) + ']/td[3]/span[2]').text.replace(', ', ''))
                        stats[4].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[4]').text)
                        stats[5].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[5]').text)
                        stats[6].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[6]').text)
                        stats[7].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[7]').text)
                        stats[8].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[8]').text)
                        stats[9].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[9]').text)
                        stats[10].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[10]').text)
                        stats[11].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[11]').text)
                        stats[12].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[12]').text)
                        stats[13].append(driver.find_element_by_xpath(
                            tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[13]').text)
                        if z == 1 or z == 2:
                            stats[14].append(driver.find_element_by_xpath(
                                tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[14]').text)
                        if z == 3:
                            stats[14].append(driver.find_element_by_xpath(
                                tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[14]').text)
                            stats[15].append(driver.find_element_by_xpath(
                                tb_id + '//*[@id="player-table-statistics-body"]/tr[' + str(a) + ']/td[15]').text)

                    time.sleep(5)

                    next_button = driver.find_element_by_xpath(paging_id + '//*[@id="next"]')

                    if str(next_button.get_attribute('class')).endswith('disabled '):
                        hasNextPage = False
                        break

                    driver.execute_script("arguments[0].click();", next_button)

                    time.sleep(5)

                except NoSuchElementException:
                    break

            row = []

            league = Select(driver.find_element_by_id('tournaments')).first_selected_option.text.replace(' ', '')
            season = Select(driver.find_element_by_id('seasons')).first_selected_option.text.replace('/', '-')

            file_name = league + '-' + category + '-' + season

            with open(os.path.join('Datasets/', file_name + '.csv'), mode='w', encoding='UTF-8') as player_file:
                employee_writer = csv.writer(player_file)

                for c in range(0, len(stats[0])):
                    for d in range(0, len(stats)):
                        row.append(stats[d][c])
                    employee_writer.writerow(row)
                    # print(row)
                    row.clear()

            # df = pd.read_csv(file_name + '.csv', encoding='ISO-8859-1')
            # pd.options.display.width = 0
            # print(df)
            print('Datasets/' + file_name + '.csv Created.')
            stats.clear()


