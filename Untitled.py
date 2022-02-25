
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.thetrainline.com/train-companies/greater-anglia')


from selenium.webdriver.common.keys import Keys

def train_min_prices(start_pnt,end_pnt):

					l = driver.find_element_by_id(start_pnt)
					#send input
					l.send_keys("Uckfield")
					#send keyboard input
					l.send_keys(Keys.RETURN)



					ar = driver.find_element_by_id(end_pnt)
					#send input
					ar.send_keys("Weymouth")
					#send keyboard input
					ar.send_keys(Keys.RETURN)



					driver.find_element_by_xpath('//*[@id="pageHeader"]/div[2]/div/form/div/button').click()
					#print("Navigating to Next Page")



					h1 = driver.find_elements_by_class_name('_18rfpwff')
					prices=[]
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







