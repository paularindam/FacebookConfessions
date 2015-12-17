#!/usr/bin/env python

# Selenium stuff
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import os
import pickle
import StringIO
import re
import urllib2
import sys
from bs4 import BeautifulSoup

def findGender(source_code,NAME):
	source = source_code.encode("utf-8")

	for line in StringIO.StringIO(source):
        	if NAME in line and "ctl00_ContentPlaceHolder1_LabelSearchedFor" in line:
            		gender1 = line.split("ctl00_ContentPlaceHolder1_LabelSearchedFor").pop()
            		if "female" in gender1:
				return "female"
			#.split('bold;">').pop().split('<')[0]
			elif "unisex" in gender1:
            			return "unisex"
			elif "male" in gender1:
				return "male"
			else:
				return "none"

for i in range(1):
	browser = webdriver.Firefox()
	browser.maximize_window()
	browser.get("http://genderchecker.com/search.aspx")
	time.sleep(3)

	name = browser.find_element_by_name("ctl00$TextBoxName")
	NAME = sys.argv[1]
	name.send_keys(NAME,Keys.RETURN)
	time.sleep(3)
	source_code = browser.page_source
	gender = findGender(source_code,NAME)
	if gender is None:
		gender = "None"
	print(NAME+":"+gender+"\n")
	browser.close()
