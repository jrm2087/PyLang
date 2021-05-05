import time
import bs4 as bs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lang_source = {
    "DE":"translator-lang-option-de",#alemán
    "BG":"translator-lang-option-bg",#búlgaro
    "CS":"translator-lang-option-cs",#checo
    "ZH":"translator-lang-option-zh",#chino
    "DA":"translator-lang-option-da",#danés
    "SK":"translator-lang-option-sk",#eslovaco
    "SL":"translator-lang-option-sl",#esloveno
    "ES":"translator-lang-option-es",#español
    "ET":"translator-lang-option-et",#estonio
    "FI":"translator-lang-option-fi",#finés
    "FR":"translator-lang-option-fr",#francés
    "EL":"translator-lang-option-el",#griego
    "HU":"translator-lang-option-hu",#húngaro
    "EN":"translator-lang-option-en",#inglés
    "IT":"translator-lang-option-it",#italiano
    "JA":"translator-lang-option-ja",#japonés
    "LV":"translator-lang-option-lv",#letón
    "LT":"translator-lang-option-lt",#lituano
    "NL":"translator-lang-option-nl",#neerlandés
    "PL":"translator-lang-option-pl",#polaco
    "PT":"translator-lang-option-pt",#portugués
    "RO":"translator-lang-option-ro",#rumano
    "RU":"translator-lang-option-ru",#ruso
    "SV":"translator-lang-option-sv" #sueco
}


lang_to = {
    "DE":"translator-lang-option-de-DE",#alemán
    "BG":"translator-lang-option-bg-BG",#búlgaro
    "CS":"translator-lang-option-cs-CS",#checo
    "ZH":"translator-lang-option-zh-ZH",#chino
    "DA":"translator-lang-option-da-DA",#danés
    "SK":"translator-lang-option-sk-SK",#eslovaco
    "SL":"translator-lang-option-sl-SL",#esloveno
    "ES":"translator-lang-option-es-ES",#español
    "ET":"translator-lang-option-et-ET",#estonio
    "FI":"translator-lang-option-fi-FI",#finés
    "FR":"translator-lang-option-fr-FR",#francés
    "EL":"translator-lang-option-el-EL",#griego
    "HU":"translator-lang-option-hu-HU",#húngaro
    "EN":"translator-lang-option-en-US",#inglés
    "GB":"translator-lang-option-en-GB",#britanico
    "IT":"translator-lang-option-it-IT",#italiano
    "JA":"translator-lang-option-ja-JA",#japonés
    "LV":"translator-lang-option-lv-LV",#letón
    "LT":"translator-lang-option-lt-LT",#lituano
    "NL":"translator-lang-option-nl-NL",#neerlandés
    "PL":"translator-lang-option-pl-PL",#polaco
    "PT":"translator-lang-option-pt-PT",#portugués
    "RO":"translator-lang-option-ro-RO",#rumano
    "RU":"translator-lang-option-ru-RU",#ruso
    "SV":"translator-lang-option-sv-SV" #sueco
}


def translater(translate,lan_source,lan_to):
    url = 'https://www.deepl.com/es/translator'
    browser = webdriver.PhantomJS('phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    browser.get(url)
    
    #btn_lang_source = browser.find_elements_by_class_name("lmt__language_select--source")[0]    
    btn_lang_source = WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CLASS_NAME,"lmt__language_select--source")))
    btn_lang_source.click()    
    print(btn_lang_source)
    time.sleep(3)
    raw_html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    target = bs.BeautifulSoup(raw_html, 'html.parser').find(class_="lmt__language_select__menu")
    
    print(target)
    WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,"//button[@dl-test='" + lang_source[lan_source] + "']")))
    #browser.find_element_by_xpath("//button[@dl-test='" + lang_source[lan_source] + "']")
    #browser.execute_script("document.getElementsByClassName('lmt__language_select__active')[0].click()")  
    #browser.execute_script("document.querySelectorAll('[dl-test=\""+lang_source[lan_source]+"\"]')[0].click()")
    
    #browser.execute_script("document.getElementsByClassName('lmt__language_select__active')[1].click()")  
    #browser.execute_script("document.querySelectorAll('[dl-test=\""+lang_to[lan_to]+"\"]')[0].click()")  
    
    time.sleep(3)
    input_area = browser.find_element_by_class_name('lmt__source_textarea')
    input_area.clear() 
    input_area.send_keys(translate)
    time.sleep(3)
    raw_html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    target = bs.BeautifulSoup(raw_html, 'html.parser').find(class_="lmt__textarea lmt__textarea_dummydiv", attrs={"id":"target-dummydiv"})
    browser.quit()
    return target.text




def main():
    print(translater("Las aves son animales vertebrados, de sangre caliente, que caminan, saltan o se mantienen solo sobre las extremidades posteriores","ES", "EN"))


if __name__ == "__main__":
    main()

