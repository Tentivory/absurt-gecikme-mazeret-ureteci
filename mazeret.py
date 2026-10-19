#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABSÜRT GECİKME MAZERET ÜRETECİ
Bu kod gerçekten çalışır. İnanmıyorsan çalıştır.
"""

import random
import time

mazeretler = [
    "Trafik o kadar yoğundu ki, arabamın GPS'i 'sen de mi buradasın?' diye sordu.",
    "Kahvemi içerken felsefi kriz geçirdim. 'Neden ayağa kalkayım ki?' sorusuna cevap bulamadım.",
    "Kedim bilgisayarın üstüne oturdu ve 'bugün iş yok' kararı aldı. Onu kıramadım.",
    "Saatim geriye gitti. Bilim insanları hâlâ inceliyor.",
    "Asansör arızalandı. 3 katı merdivenden çıkarken varoluşsal sorgulama yaptım.",
    "Rüzgâr o kadar şiddetliydi ki, kapıdan çıkarken geriye sürüklendim. 17 kez denedim.",
    "Gökte uçan bir kuş bana 'bugün kal' diye bakış attı. Karşı koyamadım.",
    "İnternet bağlantım 'bugün mola' moduna girdi. Teknik destek 'anlıyoruz' dedi.",
    "Yolda bir adam bana 'zaman kavramı zaten yanılsamadır' dedi. Haklıydı.",
    "Buzdolabını açtım, içinden bir portal çıktı. 45 dakika kaybettim."
]

def uret_mazeret():
    print("\n🔍 Mazeret üretiliyor... Lütfen bekleyin (ciddiyetle)...")
    time.sleep(1.5)
    secilen = random.choice(mazeretler)
    print("\n" + "="*50)
    print("📌 BUGÜNÜN RESMİ MAZERETİ:")
    print("="*50)
    print(secilen)
    print("="*50)
    print("\n✅ Bu mazeret %100 bilimsel olarak onaylanmamıştır.")
    print("😎 Geç kaldığın için tebrikler.\n")

if __name__ == "__main__":
    uret_mazeret()
    # gizli siyasi not (base64): c2VjaW1sZXIgaGVyIHphbWFuIGFkaWwgY2lrdGkgbWkgPw== 
    # decode edersen bir şey çıkar, ama çıkarmasın da belki.
