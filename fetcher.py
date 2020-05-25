from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

email = "seu_email@wavy.global"
senha = "sua_senha"

negocio = "ChatClub_ContaASeOlhar"

driver = webdriver.Firefox()
driver.get("https://business.facebook.com/settings/whatsapp-business-accounts/")

#fill login form
email_txt = driver.find_element_by_name("email")
email_txt.clear()
email_txt.send_keys(email)

passw_txt = driver.find_element_by_name("pass")
passw_txt.clear()
passw_txt.send_keys(senha)

passw_txt.send_keys(Keys.RETURN)

try:
	#wait for loading accounts list and click on selected one
	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[text() = '" + negocio + "']"))).click()

	#wait for loading account info and click on configurations tab
	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[text() = 'Configurações']"))).click()

	#wait for loading configuration tab
	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='_3-9a']")))

	status = driver.find_element_by_xpath("//span[@class='_3-9a']").text

	#hardcoding xpath because the divs have weird classes
	confirmacao = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div[3]/div[4]/div/div[2]/div/div").text

	analise = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div/div/div[3]/div[2]/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div[3]/div[11]/div/div[2]/div[1]/div[2]").text

	response = [status, confirmacao, analise]
except:
	print("[ERROR] Timeout error, try again later")
	response = [error]

print(response)
driver.close()