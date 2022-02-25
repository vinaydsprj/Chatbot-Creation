
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get('https://www.thetrainline.com/train-companies/greater-anglia')
driver.implicitly_wait(10)
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

					driver.implicitly_wait(10)


					driver.find_element_by_xpath('//*[@id="arrival-results"]/li[1]/button').click()


					driver.implicitly_wait(10)



					driver.find_element_by_xpath('//*[@id="pageHeader"]/div[2]/div/form/div/button').click()
					print("Navigating to Next Page")
					driver.implicitly_wait(10)


					h1 = driver.find_elements_by_class_name('_phghca')
					total_data=[]
					for i in h1:
					          # print("this is the separate data",i.text) 
					           t=i.text
					           t2=t.split('$')[1]
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
					    return min
					smallest_num_in_list(prices)


					return smallest_num_in_list(prices)





lowest_price_today=train_min_prices("Weymouth","Uckfield")

print("the lowest price for the train is ",lowest_price_today)

