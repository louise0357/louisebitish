# ARACIN YASA DIŞI KULLANIMININ SORUMLULUĞU KESİNLİKLE KULLANICIYA AİTTİR. YAPIMCI HİÇBİR SORUMLULUK KABUL ETMEMEKTEDİR.
# CODED BY LOUİSE0357

import platform
import subprocess
from termcolor import colored
import os
import sys
import pyfiglet
import random
import socket
import time

def update_github_repo():
    try:
        subprocess.check_call(["git", "reset", "--hard"])
        subprocess.check_call(["git", "pull", "origin", "main"])
        print("Tool başarıyla güncellendi.")
    except subprocess.CalledProcessError:
        print("Tool güncellenirken bir hata oluştu.")

def encode_decode_based_on_os(data, encode=True, hash_type="base64"):
    current_os = platform.system()
    try:
        if current_os == "Linux":
            if encode:
                encoded_data = subprocess.check_output(f'echo "{data}" | {hash_type}', shell=True)
            else:
                encoded_data = subprocess.check_output(f'echo "{data}" | {hash_type} -d', shell=True)
        elif current_os == "Windows":
            if encode:
                encoded_data = subprocess.check_output(f'echo "{data}" | certutil -encode{hash_type} -f -', shell=True)
            else:
                encoded_data = subprocess.check_output(f'echo {data} | certutil -decode{hash_type} -f -', shell=True)
        else:
            print("Desteklenmeyen işletim sistemi.")
            return None

        return encoded_data.decode().strip()
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e}")
        return None

def generate_wordlist(filename, keywords):
    try:
        with open(filename, 'w') as file:
            for keyword in keywords:
                variations = generate_variations(keyword)
                file.write(keyword + '\n')  
                for variation in variations:
                    file.write(variation + '\n') 
        print("Wordlist '{}' successfully created.".format(filename))
    except Exception as e:
        print("An error occurred while creating the wordlist: {}".format(str(e)))

def generate_variations(keyword):
    variations = []
    variations.append(keyword.lower()) 
    variations.append(keyword.upper()) 
    variations.append(keyword.capitalize()) 
    return variations

def scan_port(ip, port):
    porttaraniyor = colored("Port Taraması Başladı! Lütfen Bekleyin...", "red")
    print(porttaraniyor)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.close()
        print("Port {} açık".format(port))
    except socket.error:
        pass

def main_menu():
    os.system("clear")

    baslangic = colored("Tool Başlatılıyor.", "red")
    print(baslangic)
    time.sleep(1)

    os.system("clear")

    baslangic2 = colored("Tool Başlatılıyor..", "red")
    print(baslangic2)
    time.sleep(1)

    os.system("clear")

    baslangic3 = colored("Tool Başlatılıyor...", "red")
    print(baslangic3)
    time.sleep(1)
    
    os.system("clear")
    
    figlet_text = pyfiglet.figlet_format("L0UISE BITISH")
    colored_text = colored("""
    
 _     ___  _   _ ___ ____  _____   ____ ___ _____ ___ ____  _   _ 
| |   / _ \| | | |_ _/ ___|| ____| | __ )_ _|_   _|_ _/ ___|| | | |
| |  | | | | | | || |\___ \|  _|   |  _ \| |  | |  | |\___ \| |_| |
| |__| |_| | |_| || | ___) | |___  | |_) | |  | |  | | ___) |  _  |
|_____\___/ \___/|___|____/|_____| |____/___| |_| |___|____/|_| |_| v1.5
    
    """, "red")
    print(colored_text)

    colored_text_bilgi = colored("NOT: ARACIN YASA DIŞI KULLANIMI KESİNLİKLE YASAKTIR. TÜM SORUMLULUK KULLANICIYA AİTTİR.", "red")
    print(colored_text_bilgi)

    colored_text_ig = colored("""
    
İnstagram: louise0357
    """, "magenta")
    print(colored_text_ig)

    colored_text_github = colored("""Github: https://github.com/louise0357
    """, "green")
    print(colored_text_github)

    islemler = colored("""
    1: NMAP
    2: SQLMAP
    3: WİRESHARK
    4: WORDLİST CREATER
    5: MAC CHANGER
    6: PENETRASYON TESTLERİ
    7: USER AGENT GEN
    8: PORT SCANNER
    9: HASH
    0: ÇIKIŞ
    """, "cyan")
    print(islemler)

    giris_islem = colored("İşlem: ", "yellow")
    giris = input(giris_islem)

    if giris == "1":
        print("NMAP SEÇTİN:D")
        nmap_ip = input("İP: ")
        os.system("nmap -sS -sV -Pn -T4 -A" + nmap_ip)
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "2":
        print("SQLMAP (İNJECTİON) SEÇTİN:D")
        linkk = input("Link: ")
        os.system("sqlmap -u " + linkk + " --dbs --batch")
        
        devamsoru = input("Devam Etmek İstermisiniz? (Y/n): ")
        
        if devamsoru == "Y" or devamsoru == "y":
            dbnamesoru = input("Database ismini giriniz: ")
            os.system("sqlmap -u " + linkk + " -D " + dbnamesoru + " --tables --batch")
            
            devamsoru2 = input("Devam Etmek İstermisiniz? (Y/n): ")
            
            if devamsoru2 == "Y" or devamsoru == "y":
                tablenamesoru = input("Tablename Giriniz: ")
                os.system("sqlmap -u " + linkk + " -D " + dbnamesoru + " -T " + tablenamesoru + " --columns --batch")
                
                devamsoru3 = input("Devam Etmek İstermisiniz? (Y/n): ")
                
                if devamsoru3 == "Y" or devamsoru == "y":
                    columnnotcolored = colored("""Not: Birden fazla column çekmek istiyorsanız virgül ile boşluksuz yazabilirsiniz.
Örn: column1,column2,column3
""", "red")
                    print(columnnotcolored)
                    columnnamesoru = input("Column name Giriniz: ")
                    os.system("sqlmap -u " + linkk + " -D " + dbnamesoru + " -T " + tablenamesoru + " -C " + columnnamesoru + " --dump --batch")
                    
                elif devamsoru3 == "N" or devamsoru == "n":
                    main_menu()
        
            elif devamsoru2 == "N" or devamsoru == "n":
                main_menu()
        
        elif devamsoru == "N" or devamsoru == "n":
            main_menu()
        
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "3":
        print("WİRESHARK SEÇTİN:D")
        os.system("wireshark")
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "4":
        print("WORDLİST CREATER SEÇTİN:D")
        filename = input("Dosya adı: ")
        keywords = []
        while True:
            keyword = input("Anahtar kelime (çıkmak için 'q' tuşuna basın): ")
            if keyword == "q":
                break
            keywords.append(keyword)
        generate_wordlist(filename, keywords)
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "5":
        print("5 SEÇTİN XD")
        adapter_secim = input("Cihazınızın İsmini girin: ")
        os.system("macchanger -r " + adapter_secim + "")
        print("Mac Adresiniz Başarıyla Değiştirildi!")
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "6":
        print("ZAP SEÇTİN:D")
        os.system("apt install owasp-zap")
        os.system("owasp-zap")
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "7":
        print("USER AGENT GEN SEÇTİN:D")

        def generate_user_agent():
            operating_systems = [
                'Windows NT 10.0; Win64; x64',
                'Macintosh; Intel Mac OS X 10_14_6',
                'X11; Linux x86_64',
                'iPhone; CPU iPhone OS 14_5 like Mac OS X',
                'Android 11; Mobile; rv:89.0'
            ]
            operating_system = random.choice(operating_systems)

            browsers = [
                'Chrome/90.0.4430.212',
                'Safari/537.36',
                'Firefox/89.0',
                'Edge/91.0.864.59',
                'Opera/76.0.4017.123'
            ]
            browser = random.choice(browsers)

            user_agent = f'Mozilla/5.0 ({operating_system}) AppleWebKit/537.36 ({browser}) Chrome/90.0.4430.212 Safari/537.36'
            return user_agent

        user_agent = generate_user_agent()
        print(user_agent)

        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "8":
        print("PORT SCANNER SEÇTİN:D")
        ip = input("Taranacak IP adresi: ")
        for port in range(1, 1024):
            scan_port(ip, port)
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")
    
    elif giris == "9":
        print("HASH SEÇTİN:D")
        data = input("Veriyi girin: ")
        hash_type = input("Kullanmak istediğiniz hash türünü seçin (base64 için 1, base58 için 2): ")
        if hash_type == "1":
            hash_type = "base64"
        elif hash_type == "2":
            hash_type = "base58"
        else:
            print("Geçersiz hash türü seçtiniz.")
            main_menu()
        encode_decode_choice = input("Encode (1) veya Decode (2) işlemi seçin: ")
        if encode_decode_choice == "1":
            encoded_data = encode_decode_based_on_os(data, encode=True, hash_type=hash_type)
            if encoded_data:
                encodesvery = colored(f"Encode edilmiş veri: {encoded_data}", "red")
                print(encodesvery)
        elif encode_decode_choice == "2":
            decoded_data = encode_decode_based_on_os(data, encode=False, hash_type=hash_type)
            if decoded_data:
                decodesvery = colored(f"Decode edilmiş veri: {decoded_data}", "red")
                print(decodesvery)
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
        
        gecis_soru = input("Ana menüye dönmek için Enter tuşuna basın...")
        main_menu()

    elif giris == "0":
        print("Tool'dan Çıkış Yapılıyor...")
        time.sleep(3)
        sys.exit()

    else:
        print("Geçersiz İşlem. Tekrar deneyin.")
        time.sleep(2)
        main_menu()

if __name__ == "__main__":
    update_github_repo()
    main_menu()
