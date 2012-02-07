from functional_tests import FunctionalTest, ROOT
from selenium.webdriver.common.keys import Keys
import requests
import simplejson

class testAddButton(FunctionalTest):
	
	def test_add_company_from_button(self):
		# Gertrude fires up her browser and opens up the main page
		self.browser.get(ROOT)
		
		#He sees a field with the label "permalink"
		permalink_field = self.browser.find_element_by_name('permalink')
		#Enters 'spotify' in the field
		permalink_field.send_keys('spotify')
		#Hits enter...
		permalink_field.send_keys(Keys.RETURN)
		
		#Make sure that we can find the text "Spotify" on the page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Spotify', body.text)
		
		