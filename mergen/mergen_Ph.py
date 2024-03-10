import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import os
import sys
from colorama import Fore,Style



def info(mobileNo):
    mobileNo=phonenumbers.parse(mobileNo)
    print("\n")

    print(f"{Fore.BLUE}",timezone.time_zones_for_number(mobileNo))
    print(f"{Fore.GREEN}"+ Style.BRIGHT+ carrier.name_for_number(mobileNo,"en"))
    print(f"{Fore.RED}"+Style.BRIGHT+ geocoder.description_for_number(mobileNo,"en") )

    vn=phonenumbers.is_valid_number(mobileNo)
    pn=phonenumbers.is_possible_number(mobileNo)

           
    if vn == True:
            print(f"{Fore.BLUE}Valid Mobile Number:           {Style.BRIGHT}{Fore.GREEN}",phonenumbers.is_valid_number(mobileNo))
            
    elif vn == False:
            print(f"{Fore.BLUE}Valid Mobile Number:           {Style.BRIGHT}{Fore.RED}",phonenumbers.is_valid_number(mobileNo))


    if pn == True:
            print(f"{Fore.BLUE}Checking possibility of Number:{Style.BRIGHT}{Fore.GREEN}",phonenumbers.is_possible_number(mobileNo))
            
    elif pn == False:
            print(f"{Fore.BLUE}Checking possibility of Number:{Style.BRIGHT}{Fore.RED}",phonenumbers.is_possible_number(mobileNo))



    


results= []
def info_file():

    inputfile = input(f'Path to file with phone numbers to scan: {Fore.YELLOW}')
    

    with open(inputfile) as infile:
        for line in infile:
            results.append(line.strip())

    count = 0

    for i in results:
        
        print("\n")
        count += 1
        if 1 == 1:
            sys.stdout.write(Fore.RED + Style.BRIGHT+ f"[{count}][" + i + "] " +Fore.BLUE )
            print("\n")
            mobilefileNo=phonenumbers.parse(i)

            print(f"{Fore.BLUE}",timezone.time_zones_for_number(mobilefileNo))
            print(Fore.GREEN+ Style.BRIGHT+ carrier.name_for_number(mobilefileNo,"en"))
            print(Fore.RED+Style.BRIGHT+geocoder.description_for_number(mobilefileNo,"en"))
            

            vn=phonenumbers.is_valid_number(mobilefileNo)
            pn=phonenumbers.is_possible_number(mobilefileNo)

           
            if vn == True:
                print(f"{Fore.BLUE}Valid Mobile Number:           {Style.BRIGHT}{Fore.GREEN}",phonenumbers.is_valid_number(mobilefileNo))
            
            elif vn == False:
                print(f"{Fore.BLUE}Valid Mobile Number:           {Style.BRIGHT}{Fore.RED}",phonenumbers.is_valid_number(mobilefileNo))


            if pn == True:
                print(f"{Fore.BLUE}Checking possibility of Number:{Style.BRIGHT}{Fore.GREEN}",phonenumbers.is_possible_number(mobilefileNo))
            
            elif pn == False:
                print(f"{Fore.BLUE}Checking possibility of Number:{Style.BRIGHT}{Fore.RED}",phonenumbers.is_possible_number(mobilefileNo))

            print(f"{Fore.GREEN}___________________________________________")

        


def __start__():
    os.system("clear")
    print(f"{Fore.GREEN}You Are Welcome To Phone Tool ")
    print(f"{Fore.RED}[1]    Phone Info")
    print(f"{Fore.RED}[2]    Phone Info File\n")

    n = int(input(f"{Fore.RED}Please Select : {Fore.YELLOW}"))
    if n==1:
        phone_number=input(f"{Fore.RED}Please Enter Number Via + : {Fore.YELLOW}")
        info(phone_number)
    elif n==2:
        info_file()
    else:
        print(f"{Fore.RED}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")

if __name__ == '__main__':
    __start__()