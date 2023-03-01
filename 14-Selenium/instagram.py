from selenium import webdriver
from selenium.webdriver.common import keys
from instagramUserInfo import username , password
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class Instagram:
    def __init__(self,username,password):
        #tarayıcıda sayfaları ing açmak icin
        
        #self.browserProfile=webdriver.ChromeOptions()
        #self.browserProfile.add_experimental_option("prefs",{'intl.accept_languages':'en,en_US'})
        #self.browser=webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        
        self.username =username
        self.password =password
        self.browser =webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        

    def LogIn(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(2)

        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password,(Keys.ENTER))
        time.sleep(8)
        

    def getFollowers(self):

        #self.browser.get(f"https://www.instagram.com/emircantamer")
        #followersCount=self.browser.find_element(By.XPATH,'//*[@id="mount_0_0_S8"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span').text
       # followingCount=self.browser.find_element(By.XPATH,'//*[@id="mount_0_0_S8"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div/span').text
        #time.sleep(2)
             
        #print("Takipci sayısı:" + followersCount)
        #print("Takip edilen kişi sayısı: "+ followingCount)

        
        self.browser.get(f"https://www.instagram.com/emircantamer/followers/")  
        i=1
        while i<=176:
            liste=[]
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            self.browser.implicitly_wait(5)                                 
            follower=self.browser.find_element(By.XPATH,f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[1]/div/div/span/a/span/div').text
            liste=liste.append(follower)
            i=i+1
            
        print(liste)


    def followUser(self, username):
        
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)

        followButton=self.find_element(By.TAG_NAME,"button")
        if followButton.text =="Takip Et":
            followButton.click()
            time.sleep(1)
        else:
            print("zaten takiptesin")

    def unFollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton=self.browser.find_element_by_tag_name("button")
        if followButton.text=="Takiptesin":
            followButton.click()
            time.sleep(2)
            confirmButton=self.browser.find_element_by_xpath("//button[text()='Takibi bırak']").click()
        else:
            print("Zaten Takip etmiyorsunuz")
        

insta=Instagram(username, password)
insta.LogIn()
insta.getFollowers()
#insta.followUser("kod_evreni") #takip edilmesini istedigimiz kişi/kişiler
#insta.unFollowUser("kod_evreni")
