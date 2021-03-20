from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
# chrome_options.add_argument("--headless")
# firefox_options.add_argument("--headless")

browser = webdriver.Firefox()
browser.get('https://dashboard.cowin.gov.in/')

data = {}

india_total_count = browser.find_element_by_xpath('/html/body/app-root/div/div/div[2]/tabset/div/tab[1]/app-main-dashboard/div/section/div/div[1]/div[3]/div/div[2]/h3').get_attribute("innerHTML")
karnataka_daily_count = browser.find_element_by_xpath('/html/body/app-root/div/div/div[2]/tabset/div/tab[1]/app-main-dashboard/div/section/div/div[3]/section[3]/div/div[2]/div/table/tbody/tr[16]/td[2]').get_attribute('innerHTML')
# print((india_total_count))
data["India_Total_Count"] = india_total_count
data["Karnataka_Daily_Count"] = karnataka_daily_count 
print(data)
