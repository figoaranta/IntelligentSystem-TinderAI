import person_detector
import person
import tensorflow as tf
from classifier import Classifier
from selenium import webdriver
from time import sleep
from secret import username ,password
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
TINDER_URL = "https://api.gotinder.com"
token = "432358fb-0ec5-4233-8660-1bdd8235c039"
image_url= ""

user={
    "photos": [],
}



class Tinderbot():
    def __init__(self):
        self.driver = driver
        self.begining = True

    def login(self):
        self.driver.get('https://tinder.com/');

        sleep(3)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        print("fb btn clicked")
        fb_btn.click()

        #base login page
        base_window = self.driver.window_handles[0]

        #swtich to login form
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)

        lgn_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        lgn_btn.click()

        #switch to base window
        self.driver.switch_to_window(base_window) 
        
        sleep(5)
        for i in range(0,2):
            try:
                self.window_pop_up()
            except Exception:
                print("Error Occured in line 40!")
        sleep(5)


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def window_pop_up(self):
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def close_pop_up(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_4.click()

    def match_pop_up(self):
        popup_5 = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popup_5.click()
        print("lol")
        
    def tinder_gold_pop_up(self):
        popup_6 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]');
        popup_6.click()

    def out_of_like_pop_up(self):
        popup_7 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        popup_7.click()
    
    def max_like(self):
        maxlike_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[1]')
        maxlike_btn.click()

    def get_image_path(self):
        body = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div')
        rawURL = body.get_attribute('style')
        return rawURL;

    def get_url(self,rawUrl):
        string = ""
        imageURL = ""
        for char in rawUrl:
            if char == ";":
                break
            else:
                string = string + char
        count = 0
        for char in string:
            if char == '"':
                count += 1
            elif count == 1:
                imageURL = imageURL + char

        return imageURL
    def next_image():
    	switch_frame = driver.switch_to.frame(driver.find_element_by_name('gsft_main'))

        next_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[2]')
        print(next_btn)
        next_btn.click()

    def auto_like(self):
        while True:
            sleep(10)
            try:
                rawURL = self.get_image_path()
                image_url = self.get_url(rawURL)
                print(image_url)
                print(len(user['photos']))
                if len(user['photos'])==0:
                	user['photos'].append(image_url)
                else:
                	if image_url == user['photos'][len(user['photos']-1)]:
                		print(user['photos'])
                		self.dislike()
                print("work until here")
                self.next_image()
                

                user['photos'].pop()
            except Exception:
                try:
                    self.close_pop_up() 
                except Exception:
                    try:
                        self.match_pop_up()
                    except Exception:
                        try:
                            self.window_pop_up()
                        except Exception:
                            # self.out_of_like_pop_up()
                            break;
                                                        
                                    
                                

bot = Tinderbot()
bot.login()
bot.auto_like()