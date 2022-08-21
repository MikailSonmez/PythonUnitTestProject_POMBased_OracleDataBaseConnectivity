import time

import cx_Oracle

import os

from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] = 'C:\\ way of path I dont have Oracle'


driver = webdriver.Chrome()

driver.get("https://newtours.demoaut.com/")
driver.maximize_window()


# Establish connection to the database

con = cx_Oracle.connect("hr", "hr", "localhost/pdborc1")

cur = con.cursor()

query = "select * From users"

cur.execute(query)

for cols in cur:
    driver.find_element(By.NAME, "userName").send_keys(cols[0])
    driver.find_element(By.NAME, "password").send_keys(cols[1])
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)

    # validation started
    if driver.title == "Fint a Flight: Mercury Tours:":
        print("Test passed")
    else:
        print("Test failed")
    driver.find_element(By.LINK_TEXT, "Home").click()


cur.close()
con.cluse()

print("Completed!!!")
