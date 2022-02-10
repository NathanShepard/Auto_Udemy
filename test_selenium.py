from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox()
driver = webdriver.Chrome('/Users/nathanshepard/Downloads/chromedriver')

url = 'https://newyork.craigslist.org/'


driver.get(url)
# css selector
# .sublinks > li:nth-child(2) > a:nth-child(1)
# css path.
# html.js.canvas.draggable.fileAPI.geolocation.matchMedia.picture.pushState.placeholder.no-touchCapable.transitions body.homepage.en.desktop.w1024 div.wrapper section.page-container nav#topban.regular div.regular-area ul.sublinks li a

driver.find_element_by_xpath('//*[@id="topban"]/div/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="ccc1"]/li[2]/a/span').click()
