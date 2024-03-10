import os
from colorama import Fore
import time
import sys

def Banner():

    os.system("clear")
    
    print(Fore.LIGHTRED_EX+"""\n    
                                                                                          
       +%-      ##     %*   .%#              -#-        +#.  -#-   ##             -#-     
   .-+%%%%#+-.  =%-    %#    :%#:            =%-        +%.  -%=   :%#:            *%-    
   ++- +%-.-+=  -%+    %#      +%#=.   =#+-::+%-        +%.  -%=     =%#=.    .:    *%:   
     .+%%%=     -%*+*#%%#       .#%%   #%=+*#%%-   *%%%%%%%%%%%:      .#%%:  -%#.    %%   
   _+%*   #%=   :**=:.:%#     .+%*-    *%    =%-   %%   *%:         .+%*-.  .%#      *%:  
    *%+   *%+          %#    -%#.      %%    =%-   %%   +%.        :%#:      %#.    :%#   
     .*%#%+.           #+   .#*       :#=    -#-   ##   +%.        ##        .*%%##%#=   
      
        ====================================================================
        **                                                                **
        **                 Developers : Bozkurt                           **
        **                                                                **
        **                 Git-Hub    :https://github.com/ozan-B          **
        **                                                                **
        ====================================================================          
                """)       



def banner():
    print("""\033[96m
      ooooooo                oooooooo                        oooooooooo  
    o888   888o ooooooooooo         o   oo oooooo            888    888 
    888     888      8888    ooooo888   888   888 ooooooooo 888oooo88  
    888o   o888   8888     888    888   888   888           888    888 
      88ooo88   o888ooooooo 88ooo88 8o o888o o888o         o888ooo888  
\033[0m""")
    


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

def menu():
    slowprint(f'''
                            {Fore.LIGHTRED_EX} [1] Find Social Account 
                            {Fore.LIGHTGREEN_EX} [2] Image meta Data Information
                            {Fore.LIGHTYELLOW_EX:} [3] IP Information
                            {Fore.LIGHTBLUE_EX} [4] Phone Number Information 
                            {Fore.LIGHTMAGENTA_EX} [5] Reverse IP 
                            {Fore.LIGHTCYAN_EX} [6] Robots Scanner 
                            {Fore.LIGHTWHITE_EX} [7] CMS Scanner 
                            {Fore.BLUE} [8] Scan Wordpress Site Pluggin And Username 
                            {Fore.YELLOW} [9] Admin Panel and Subdomain Scanner 
                            {Fore.CYAN} [E] Exit . . . 

                            {Fore.RED} [{Fore.BLUE}${Fore.RED}]{Fore.CYAN} Choose one of the options above)

        ''')
    time.sleep(0.2)
    option = input("\n\n \033[93m           Let's Start \033[96m --> --> --> \033[91m ")
    
    return option



def back():
    job = input(f"\n{Fore.BLUE}Press 'b' to go menu  or Press 'a' use to again tool:    ") 
    return job


def infolist2():

    Banner()
    
    


    while True:

        op=menu()
        if op == "1":

            while True:     

                os.system("./mergen/mergen_Find_Social_account.sh") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()


        elif op == "2":

            while True:
                os.system("./mergen_IMGexif.sh") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()
            

        elif op == "3":

            while True:
                os.system("python3 mergen_IPF.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()


        elif op == "4":

            while True:
                os.system("python3 mergen_Ph.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()

        elif op == "5":

            while True:
                os.system("python3 mergen_Reverse_Ip.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()

        elif op == "6":

            while True:
                os.system("python3 mergen_Robots.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()

            
        elif op == "7":

            while True:
                os.system("python3 mergen_cms_detect.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()


        elif op == "8":

            while True:
                os.system("python3 mergen_wordpress.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()


        elif op == "9":

            while True:
                os.system("python3 mergen_admin_panel_finder.py") # Error
                user_input = back()
                if user_input == 'b' or user_input == 'B':
                    os.system('clear')
                    break
                elif user_input == 'a' or user_input == 'A':
                    os.system('clear')
                    continue
                else:
                    print("Good By :)")
                    exit()



        elif op == "E" or op== "e":
            print("[INFO] Exitting...")
            break

        else:
            print(f"{Fore.RED}[FAIL] Invalid Command Dedected. Please Input Valid Commands.") # Error
            break




     

        


infolist2()