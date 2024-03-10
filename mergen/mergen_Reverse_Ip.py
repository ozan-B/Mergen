import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from prettytable import PrettyTable
from colorama import Fore



def reverse_ip_lookup_apisiz():
        # Sonuçları tablo şeklinde görüntülemek için PrettyTable nesnesi oluştur

    print(Fore.RED+" [!] Enter Domain\n")
        
    domain = input(Fore.RED+"Reverse İp"+Fore.WHITE+"$ ")
    result_table = PrettyTable()
    result_table.field_names = ["DOMAIN", "RESOLVED DATE"]

    

    # Selenium ile domaini siteye yaz.
    # Chrome tarayıcısını başsız modda başlat
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Hedef web sitesini ziyaret etme
    url = f"https://viewdns.info/reverseip/?host={domain}&t=1"
    driver.get(url)
    time.sleep(2)

    try:
        # Sayfa açıldıktan sonra bekleme
        time.sleep(3)

        # Sayfanın tam HTML içeriğini al
        html_content = driver.page_source

    except Exception as e:
        print(f'Hata: {e}')

    # HTML içeriğini Beautiful Soup ile parse et
    soup = BeautifulSoup(html_content, 'html.parser')

    # Tüm işime yarayacak nesneleri al
    objects = soup.find('table', border='1')

    # Tablonun içindeki hücreleri bul
    cells = objects.find_all('td')

    # Hücre verilerini düzenli bir şekilde al
    domain_data = []
    current_domain = ""
    for cell in cells:
        cell_text = cell.text.strip()
        if cell_text.endswith((".com", ".ir",".tk",".net", ".tr", ".online", ".xyz", ".org", ".site",".biz",".edu",".gov",".mil",".co",".io",".info",".biz")):
            current_domain = cell_text
        elif current_domain and cell_text:
            result_table.add_row([current_domain, cell_text])
            domain_data.append([current_domain, cell_text])
            
    # Hücre verilerini ekrana yazdır
    # Satır sayısını ekrana yazdır
    num_rows = len(result_table.get_string().split('\n')) - 4
    print(f"\033[92mBu sunucuda {num_rows} adet domain barındırılmaktadır.\n")
    print(f"\033[91m{result_table}")
    print("\n")

reverse_ip_lookup_apisiz()





