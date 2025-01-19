from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import App.Config

 
import App.Config
from Frames.Status import *
from Download_Result import *


url = "http://14.139.121.219/sukresult/"

class Download_Result:
    
    def download(file_path,label):
        
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "plugins.always_open_pdf_externally": True,
            "download.default_directory":  "F:\\C & C++\\Result_Analyser\\pdf",
            "download.prompt_for_download": False
        })
       

        driver = webdriver.Chrome(options=chrome_options)

        file_path = App.Config.get_file_path()

        with open(file_path, 'r') as file:
            for current_line_number, line in enumerate(file, 1):
                    val=line[:10]

                    driver.get(url)

                    input_field = driver.find_element(By.ID, 'PRNNO')
                    submit_button = driver.find_element(By.NAME, 'Sign In')

                    input_field.send_keys(val)

                    submit_button.click()

                    try:
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pdfEmbedElement')))
                        driver.back()
                    except Exception as e:
                        print("Error: ", e)
                        
        image = Image.open(r'F:\C & C++\Result_Analyser\ok_alert.png')
        image = image.resize((20, 20), Image.LANCZOS)
        icon = ImageTk.PhotoImage(image)
 
        
        label.config(text="Result Downloaded", image=icon, compound='right',height=2,padx=5, pady=15)
        label.image = icon