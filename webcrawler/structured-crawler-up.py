# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import time
from multiprocessing import Pool
from selenium.common.exceptions import NoSuchElementException

# Load the dataset
filepath = r"E:/gas leak project/webcr/sample.xlsx"
dataset = pd.read_excel(filepath)
dataset = dataset.fillna('')   # convert missing value from NaN to empty string
dataset['BIN Number'] = 'Not found'  # Pre-Assign the BIN number to Not found

# Prepare the parameter
address_list = []
for i in range(len(dataset)):
    housenum = int(dataset.iloc[i, 1])
    streetnum = (str(dataset.iloc[i, 2])+" "+str(dataset.iloc[i, 3])+" "+str(dataset.iloc[i, 4])).strip()
    address_list.append((i, housenum, streetnum))

def get_content(address):
    # Load a web-driver
    driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    url = r'https://a810-dobnow.nyc.gov/publish/#'

    driver.get(url)
    driver.find_element_by_id("housenumber").clear()
#    time.sleep(1)

    driver.find_element_by_id("streetnumber").clear()
#    time.sleep(1)

    driver.find_element_by_id("housenumber").send_keys(address[1])
#    time.sleep(1)

    driver.find_element_by_id("streetnumber").send_keys(address[2])
#    time.sleep(1)

    # Click the button
    sel = driver.find_element_by_xpath("//select[@id='sel1']")
    Select(sel).select_by_value("1")
    driver.find_element_by_tag_name('button').click()

    # BIN obtain
    time.sleep(5)  # Must sleep until the page finished loading, otherwise xpath can not found
    try:
        BIN = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div").text[5:]
    except NoSuchElementException as e:
        BIN = -1                                       
    # Record the value
    BIN_list = (address[0], BIN)
    driver.quit()

    return BIN_list

if __name__ == '__main__':

    pool = Pool(2)
    total = pool.map(get_content, address_list)
    pool.terminate()
    pool.join()

    df = pd.DataFrame.from_records(total)
    df.rename(columns={0: 'index', 1: 'BIN Number'}, inplace=True)

    new = dataset.merge(df, how='left', left_index=True, right_on='index')

# Output to local excel file
# storepath = '/Users//Desktop/'
# dataset.to_csv(storepath + 'output.csv')



