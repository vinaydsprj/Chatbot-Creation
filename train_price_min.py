
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



					ar = driver.find_element_by_id("arrival")
					#send input
					ar.send_keys(end_pnt)
					#send keyboard input
					ar.send_keys(Keys.RETURN)


					driver.find_element_by_xpath('//*[@id="arrival-results"]/li[1]/button').click()



					driver.find_element_by_xpath('//*[@id="pageHeader"]/div[2]/div/form/div/button').click()
					print("Navigating to Next Page")



					h1 = driver.find_elements_by_class_name('_18rfpwff')
					prices=[]
					print(prices)
					for i in h1:
					       # print(i.text) 
					        t=i.text
					        t2=t.split('$')[1]
					        #print(t2)
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





train_min_prices("Weymouth","Uckfield")

