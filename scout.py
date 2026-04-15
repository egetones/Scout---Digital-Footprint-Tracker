import requests
from colorama import Fore, Style, init

# Renklendirmeyi başlat
init(autoreset=True)

print(Fore.CYAN + """
#######################################
#  SCOUT - Digital-Footprint-Tracker  #
#######################################
""")

def kullanici_kontrol(username):
    # AYARLAR:
    # url: Kontrol edilecek adres
    # check_error_text: Eğer sayfada bu yazı varsa, kullanıcı YOK demektir (200 dönse bile).
    # None ise sadece durum koduna (404) bakılır.
    
    siteler = {
        "Instagram": {
            "url": f"https://www.instagram.com/{username}/",
            "check_error_text": "Instagram photos and videos" # Instagram bazen login'e atar, bu basit bir kontrol.
        },
        "Twitter/X": {
            "url": f"https://twitter.com/{username}",
            "check_error_text": "This account doesn’t exist"
        },
        "GitHub": {
            "url": f"https://github.com/{username}",
            "check_error_text": None
        },
        "Facebook": {
            "url": f"https://www.facebook.com/{username}",
            "check_error_text": "This content isn't available right now"
        },
        "Twitch": {
            "url": f"https://m.twitch.tv/{username}",
            "check_error_text": "Tap to unmute" # Mobilde içerik yoksa bu yazı gelmez
        },
        "Steam": {
            "url": f"https://steamcommunity.com/id/{username}",
            "check_error_text": "The specified profile could not be found"
        },
        "Spotify": {
            "url": f"https://open.spotify.com/user/{username}",
            "check_error_text": "Page not found"
        },
        "Pinterest": {
            "url": f"https://www.pinterest.com/{username}/",
            "check_error_text": None
        },
        "SoundCloud": {
            "url": f"https://soundcloud.com/{username}",
            "check_error_text": "We can’t find that user"
        }
    }

    print(f"{Fore.YELLOW}[*] '{username}' için gelişmiş tarama başlatılıyor...\n")

    found_count = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5' # Hata mesajlarını İngilizce yakalamak için
    }

    for site_adi, data in siteler.items():
        url = data["url"]
        error_text = data["check_error_text"]
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            # Durum 1: Site 404 Döndürürse -> Kesin Yoktur
            if response.status_code == 404:
                print(f"{Fore.RED}[-] {site_adi}: Bulunamadı (404)")
            
            # Durum 2: Site 200 Döndürürse -> Var olabilir ama kontrol etmeliyiz
            elif response.status_code == 200:
                
                # Eğer özel bir hata metni tanımlıysa ve sayfada bu metin VARSA -> Aslında Yoktur
                if error_text and error_text in response.text:
                    print(f"{Fore.RED}[-] {site_adi}: Bulunamadı (Sahte Pozitif Yakalandı!)")
                
                # Hata metni yoksa -> Başarıyla Bulundu
                else:
                    print(f"{Fore.GREEN}[+] {site_adi}: BULUNDU -> {url}")
                    found_count += 1
            
            else:
                print(f"{Fore.WHITE}[?] {site_adi}: Farklı Cevap ({response.status_code})")
                
        except requests.exceptions.RequestException:
            print(f"{Fore.RED}[!] Hata ({site_adi}): Bağlantı zaman aşımına uğradı.")

    print(Fore.CYAN + "-" * 30)
    print(f"{Fore.YELLOW}Tarama Bitti! Toplam bulunan hesap: {found_count}")

# Kullanıcıdan input al
hedef_kullanici = input("Hedef Kullanıcı Adı: ")
kullanici_kontrol(hedef_kullanici)
