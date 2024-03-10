import requests
from colorama import Fore
import colorama
from tqdm import tqdm
import argparse
import threading
import time
import datetime

#ADMİN PANELİ taraması ve subdomain taraması yapar . 


def logo():
    print(Fore.RED+"""
     _       _           _       _____ _           _           
    / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ 
   / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|
  / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |   
 /_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_|   
                                                               

By Bozkurt


""")    
    


def findPanel(url):
    wordlist = open("admin-directory.txt","r")  #Bu kısıma kendi wordlistini ekleyebilirsin 
    for words in wordlist:
        words = words.strip()
        req = requests.get(url+words)
        if req.status_code == 200:
            print(Fore.GREEN+req.url)
        '''else:
             print(Fore.RED+url+"   status code :"+str(req.status_code))'''
        

def sub_domains(url):
    wordlist = open("admin-subdomain-list.txt","r")  #Bu kısıma kendi wordlistini ekleyebilirsin 
    for words in wordlist:
        words = words.strip()
        req = requests.get(url+words)
        if req.status_code == 200:
            print(Fore.GREEN+req.url)
        '''else:
             print(Fore.RED+url+"   status code :"+str(req.status_code))'''   





def main_func():

    logo()
    
    print(Fore.YELLOW+" 1-Admin Panel scanning")
    print(Fore.YELLOW+" 2-Subdomains scanning\n")

    option = input(Fore.BLUE+"Make Your Choice   ")
    print("\n")

    if option == "1":
        print("Sample Url : https://ornek.com/")
        url = input(Fore.RED+"Enter Url  :")


        if url:  # URL boş olup olmadığını kontrol eder
            # URL boş değilse devam edilir
            for i in range(2):
                t = threading.Thread(target=findPanel,args=(url,))
                t.start()


            
        else:
            print("Wron Choice, please try again")
            # URL boş ise istenen işlem yapılmaz veya kullanıcıya bir hata mesajı gösterilir




    elif option == "2":
        print("Sample Url : https://ornek.com/")
        url = input(Fore.RED+"Enter Url :")


        if url:  # URL boş olup olmadığını kontrol eder
            # URL boş değilse devam edilir
            for i in range(2):
                t = threading.Thread(target=sub_domains,args=(url,))
                t.start()


            
        else:
            print("The entered URL is empty.")
            # URL boş ise istenen işlem yapılmaz veya kullanıcıya bir hata mesajı gösterilir


    else:
        print("Wron Choice, please try again")




main_func()
