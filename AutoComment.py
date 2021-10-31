from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.instagram.com")
driver.set_window_position(-3,0)
driver.set_window_size(800,1150)
sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
sleep(2)

username = driver.find_element_by_name('username')
username.send_keys('')  # <- INSERT YOUR INSTAGRAM USERNAME HERE
password = driver.find_element_by_name('password')
password.send_keys('')  # <- INSERT YOUR INSTAGRAM PASSWORD HERE

login = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
sleep(4)

notnow = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()

driver.get('')  # <- LINK OF THE POST HERE

sleep(2)
comments = ""  # <- THE COMMENT YOU WANT

sleep(2)
comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
comment.click()
sleep(1)
comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
comment.click()
sleep(1)
comment.send_keys(comments)
sleep(1)
sendComment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')
sendComment.click()
sleep(2)
