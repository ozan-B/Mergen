import requests, builtwith
from colorama import Fore
import sys
def __start__():
    print(Fore.RED+" [!] Plase Enter Domain")
    target = input(Fore.RED+"└──╼"+"CMS-Detect"+Fore.WHITE+"$ ")
    if not 'https://' in target or not 'http://' in target:
        target = 'http://'+target
    info = builtwith.parse(target)


    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(Fore.BLUE+"\n"+name+': '+value)

__start__()
