from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import os

def test_scores_archive():
    global scoreid
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get('http://127.0.0.1:5000')
    scoreid = driver.find_element_by_id("score").text
    if 0 < int(scoreid) < 1000:
        return True
    else:
        return False


def main_function():
    test_scores_archive()
    if test_scores_archive() == True:
        print("Everyhing seems fine")
        sys.exit(0)
    else:
        print("Something wrong!")
        sys.exit(-1)


main_function()
