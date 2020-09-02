from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
class Instagram():
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_language':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        emailInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(2)
    
    def getFollowers(self):
         time.sleep(3)
         self.browser.get("https://www.instagram.com/{}".format(self.username))
         time.sleep(3)

         followersLink =self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
         time.sleep(3)
         dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
         
         followerCount = len(dialog.find_elements_by_css_selector("li"))
         print(followerCount)
         action = webdriver.ActionChains(self.browser)
         while True:
            dialog.click()
            print("Dialoga tıklama atıldı")
            action.send_keys(Keys.SPACE)
            action.send_keys(Keys.SPACE)
            print("Space basıldı")
           
            scrollFollowers = dialog.find_elements_by_css_selector("li")
            newCount = len(scrollFollowers)

            if (followerCount != newCount):
                followerCount = newCount
                print("new count:{}".format(followerCount))
                time.sleep(2)
            else:
                break
            

         followers = dialog.find_elements_by_css_selector("li")
         for user in followers:
             link = user.find_element_by_css_selector("a").get_attribute("href")
             print(link)
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/{}".format(username))
        time.sleep(2)

        followButton = self.browser.find_elements_by_tag_name("button")
        if(followButton.text != "Following"):
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")
    
    def unfollerUser(self,username):
        self.browser.get("https://www.instagram.com/{}".format(username))
        time.sleep(2)
        followButton = self.browser.find_elements_by_tag_name("button")
        if(followButton.text =="Following"):
            followButton.click()
            time.sleep(2)
            self.browser.find_elements_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print("Zaten takip etmiyorsunuz")

instagram = Instagram(username,password)
instagram.signIn()
instagram.getFollowers()
#instagram.followUser("deneme")