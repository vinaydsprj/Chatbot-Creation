
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36')



#,chrome_options=chrome_options

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(20)
driver.get('https://www.thetrainline.com/train-companies/greater-anglia')
# driver.get_screenshot_as_file("screenshot.png")
driver.implicitly_wait(20)
# driver.get_screenshot_as_file("screenshot01.png")
driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()


from selenium.webdriver.common.keys import Keys

def train_min_prices(start_pnt,end_pnt):

					l = driver.find_element_by_id("departure")
					#send input
					l.send_keys(start_pnt)
					#send keyboard input
					l.send_keys(Keys.RETURN)

					driver.find_element_by_xpath('//*[@id="departure-results"]/li/button').click()

					#//*[@id="departure-results"]/li/button
					driver.implicitly_wait(10)



					ar = driver.find_element_by_id("arrival")
					#send input
					ar.send_keys(end_pnt)
					#send keyboard input
					ar.send_keys(Keys.RETURN)

					driver.implicitly_wait(20)


					driver.find_element_by_xpath('//*[@id="arrival-results"]/li[1]/button').click()


					driver.implicitly_wait(20)



					driver.find_element_by_xpath('//*[@id="pageHeader"]/div[2]/div/form/div/button').click()
					# print("Navigating to Next Page")
					driver.implicitly_wait(20)


					h1 = driver.find_elements_by_class_name('_ws6660')
					# print('_phghca --> _ws6660 ')
					link = driver.current_url
					# print(h1.text)
					total_data=[]
					for i in h1:
					          # print("this is the separate data",i.text) 
					           	t=i.text
					           	t2=t.split('£')[1]
							  	# print('vinay')
					           	print(t2)
					           	total_data.append(t2)
					#print(total_data)
					prices=[]
					for i in total_data:
					       # print(i.text) 
					       # t=i.text
					        t2=i.split('\n')[0]
					       # print(t2)
					        prices.append(t2)
					def smallest_num_in_list( prices ):
					    min = float(prices[ 0 ])
					    for a in prices:
					        a=float(a)
					        if a < min:
					            min = a
						# print(min)
					    return min
					smallest_num_in_list(prices)


					return smallest_num_in_list(prices) ,link





# lowest_price_today , link =train_min_prices("Norwich","London")
#
# print("the lowest price for the train is ",lowest_price_today)
#
# print("Use this link to book the ticket: ", link)

