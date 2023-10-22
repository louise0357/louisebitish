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
import pyautogui
import scapy.all as scapy
import hashlib

def update_github_repo():
    try:
        subprocess.check_call(["git", "reset", "--hard"])
        subprocess.check_call(["git", "pull", "origin", "main"])
        print("Tool başarıyla güncellendi.")
    except subprocess.CalledProcessError:
        print("Tool güncellenirken bir hata oluştu.")

def md5_encode(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()


def ağ_analizi():
    wifi_kart_colored = colored("Wifi Kartınızın İsmini Giriniz: ", "yellow")
    wifi_kart = input(wifi_kart_colored)
    pyautogui.press("f11")
    tamekran = input(colored("Lütfen Terminal Tam Ekrana Alındıktan Sonra Enter'a Basınız.  "))
    print(colored("Ağ Analizi Başlatılıyor...", "red"))
    print(colored("Tooldan çıktıktan sonra halen tam ekranda iseniz f11 tuşuna basınız.", "cyan"))
    print("\tZaman\t\tProtokol\tKaynak IP\tHedef IP\tKaynak Port\tHedef Port\tVeri Boyutu (byte)")

    try:
        def paket_yakala(packet):
            if packet.haslayer(scapy.IP):
                zaman = time.strftime("%Y-%m-%d %H:%M:%S")
                protokol = packet[scapy.IP].proto
                ip_src = packet[scapy.IP].src
                ip_dst = packet[scapy.IP].dst
                kaynak_port = 0
                hedef_port = 0
                veri_boyutu = len(packet)

                if protokol == 6:  # TCP
                    kaynak_port = packet[scapy.TCP].sport
                    hedef_port = packet[scapy.TCP].dport
                elif protokol == 17:  # UDP
                    kaynak_port = packet[scapy.UDP].sport
                    hedef_port = packet[scapy.UDP].dport

                print(colored(f"{zaman}\t{protokol}\t\t{ip_src}\t{ip_dst}\t{kaynak_port}\t\t{hedef_port}\t\t{veri_boyutu}", "red"))

        scapy.sniff(iface=wifi_kart, store=False, prn=paket_yakala)
    except KeyboardInterrupt:
        print(colored("\nAğdaki Paket Takibi Sonlandırıldı.", "red"))


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

def port_tarama(hedef_ip, baslangic_port, bitis_port):
    for port in range(baslangic_port, bitis_port + 1):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(0.1)

        sonuc = soket.connect_ex((hedef_ip, port))

        if sonuc == 0:
            acik_port = colored(f"Port {port} açık", "red")
            print(acik_port)
        soket.close()
        

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
|_____\___/ \___/|___|____/|_____| |____/___| |_| |___|____/|_| |_| v1.9
    
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
    3: AĞ ANALİZİ
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
        print("Nmap Seçildi.")
        nmap_ip = input("İP: ")
        os.system("nmap -sS -sV -Pn -T4 -A" + nmap_ip)
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "2":
        print("Sqlmap Seçildi.")
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
        print("Ağ Analizi Seçildi.")
        ağ_analizi()
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "4":
        print("Wordlist Creater Seçildi.")
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
        print("Macchanger Seçildi.")
        adapter_secim = input("Cihazınızın İsmini girin: ")
        os.system("ifconfig " + adapter_secim + " down")
        os.system("macchanger -r " + adapter_secim + "")
        os.system("ifconfig " + adapter_secim + " up")
        print("Mac Adresiniz Başarıyla Değiştirildi!")
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "6":
        print("Penetrasyon Testleri Seçildi.")
        os.system("apt install owasp-zap")
        os.system("owasp-zap")
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")

    elif giris == "7":
        print("User Agent Generator Seçildi.")

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
        print("Port Scanner Seçildi.")
        hedef_ip = input("Hedef IP adresini girin: ")
        baslangic_port = int(input("Başlangıç portunu girin: "))
        bitis_port = int(input("Bitiş portunu girin: "))
        
        port_tarama(hedef_ip, baslangic_port, bitis_port)
        
        gecis_soru = input("Restart? (Y/n): ")
        if gecis_soru == "Y" or gecis_soru == "y":
            main_menu()
        elif gecis_soru == "N" or gecis_soru == "n":
            print("Çıkış Yapılıyor..")
    
    elif giris == "9":
        print("Hasher Seçildi.")
        data = input("Veriyi girin: ")
        hash_type = input("Kullanmak istediğiniz hash türünü seçin (base64 için 1, base58 için 2, MD5 için 3): ")
        if hash_type == "1":
            hash_type = "base64"
        elif hash_type == "2":
            hash_type = "base58"
        elif hash_type == "3":
            encoded_text = md5_encode(data)
            print("MD5 hash değeri: ", encoded_text)
            input()
            main_menu()
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
