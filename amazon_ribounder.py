from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# selenium 4.0 ↑
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = Options()

# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options) 

HREFS = []

# URL開く
driver.get("https://www.amazon.co.jp/ref=nav_logo")

# 待機処理
# driver.implicitly_wait(10)
sleep(10)
# wait = WebDriverWait(driver=driver, timeout=60)

#検索窓 
Word = "サッカー　リバウンダー"
print(Word)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Word)
sleep(1)
driver.find_element(By.ID,"nav-search-submit-button").click()

#商品URLの取得 
URLS = driver.find_elements(By.CSS_SELECTOR,"a.a-link-normal.s-no-outline")

for URL in URLS:
    URL = URL.get_attribute("href")
    print("[INFO] URL :", URL)
    HREFS.append(URL)

#商品詳細の取得 
d_list=[]

for HREF in HREFS:
    driver.get(HREF)
    # title
    title = driver.find_element(By.ID, "productTitle").text
    print("[INFO]  title :", title)
    # price 
    price = driver.find_element(By.CSS_SELECTOR, 'div.aok-align-center > span > span > span.a-price-whole').text
    print("[INFO]  price :", price)
    # img
    img = driver.find_element(By.XPATH, '//div[@id="imgTagWrapperId"]/img').get_attribute("src")
    print("[INFO]  img :", img)    
    ster = driver.find_element(By.CLASS_NAME, 'a-size-base a-color-base').text
    print("[INFO] ster :", ster)
    detail = driver.find_element(By.CLASS_NAME, 'a-list-item').text
    print("[INFO] detail :",detail)
    #d={
    #    'title':title,
    #    'price':price,
    #    'img':img,
    #    'ster':ster,
    #    'detail':detail        
    #    }
#d_list.append(d)

#print(d)
#df=pd.DataFrame(d_list)
#df_URL = pd.DataFrame({'URL':HREFS})
#df2=pd.DataFrame(d_list2)
#df3=pd.concat([df1, df2], axis=1)
#df_concat= pd.concat([df, df_URL], axis=1)
#df.to_csv("amazon_keybord_arr.csv",encoding='utf-8-sig')
#df_URL.to_csv("amazon_keybord_url.csv",encoding='utf-8-sig')
#df_concat.to_csv("amazon_rebounder.csv",encoding='utf-8-sig')