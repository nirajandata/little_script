from selenium import webdriver
import time
import random
from messages import messages

def cmt_bot():
    userId = "your email here" #enter your email there
    password = "your password" # type your password there
    browser = webdriver.Chrome(r"C:\Users\niraj\Downloads\chromedriver_win32\chromedriver.exe")
    
    story_fbid= "204394077883813"
    id = "100049396673165"
    postURL = r"https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fstory.php%3Fstory_fbid%3D" + story_fbid + "%26id%3D" + id + "&ref=104&rs=26&rid=" + id +"&refsrc=https%3A%2F%2Fm.facebook.com%2Fstory.php&refid=52"
    browser.get(postURL)
    userIdField = browser.find_element_by_id("m_login_email")
    passwordField = browser.find_element_by_id("m_login_password")    
    loginButton = browser.find_elements_by_tag_name("button")[0]
    userIdField.send_keys(userId)
    passwordField.send_keys(password)
    loginButton.click()
    time.sleep(10)
    for i in range(500):
        time.sleep(3)
        commentBox = browser.find_element_by_id("composerInput")
        commentBox.send_keys(random.choice(messages))
        time.sleep(1)
        sendButton = browser.find_elements_by_tag_name("button")[0]
        sendButton.click()
        
cmt_bot()
