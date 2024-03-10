#!/bin/bash



# Renkli metinler için ANSI renk kaçış kodları
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RESET='\033[0m'

# Renkli mesajları yazdıran fonksiyon
print_color_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${RESET}"
}

print_color_message $RED "Please enter the image file path:" 

#Kullanıcıdan giriş al
read dosya




echo -e "\n"


# exiftool çıktısını bir değişkene atama
exif_output=$(exiftool -a -s "$dosya")

print_color_message $GREEN "$exif_output"