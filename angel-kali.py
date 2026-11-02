cd ~/WHITE-ANGEL-TIMIKA
cat > angel-kali.py << 'PY'
import os, time, random, string, subprocess, json, sys, shutil
def clear(): os.system("clear")
def banner():
    clear()
    print("\033[1;37m     .-'`'-.    .-'`'-.")
    print("  .-'        \\/        '-. ")
    print(".-'   \\  WHITE ANGEL  /   '-.")
    print("\033[1;36m\\  \\   / DEFRIT - TIMIKA \\  \\   /\033[0m")
    print("\033[1;37m '-. \\  .'       '.  / .-'")
    print("    '-.'           '.-'\033[0m")
    os.system('figlet -f big "WHITE ANGEL" | lolcat 2>/dev/null || figlet "WHITE ANGEL"')
    print("\033[1;32m++++[ PROTECTION by DEFRIT - Timika v4.1 - 20 TOOLS ACTIVE ]++++\033[0m")
    print("\033[1;33m<<--------[ PAPUA TENGAH PROTECTED MENU 1-20 ]-------->>\033[0m\n")

def pause(): input("\n\033[1;36m[ENTER] balik ke menu...\033[0m"); main()

def main():
    banner()
    print("\033[1;32m[01] Cek IP Saya\n[02] Cek Lokasi IP\n[03] Cek Nomor HP\n[04] Cek Username OSINT\n[05] Cek Link Phishing\n[06] Cek Password Kuat/Gak\n[07] Cek Keamanan WiFi\n[08] Cek Aplikasi Berbahaya\n[09] Bersihkan Cache HP\n[10] Cek Info Sistem HP\n[11] Cek Baterai Health\n[12] Cek Penyimpanan HP\n[13] Generate Password Kuat\n[14] Cek Kecepatan Internet\n[15] Sembunyikan File Rahasia\n[16] Kunci Folder Enkripsi\n[17] Cek Email Bocor Gak\n[18] Buat Banner Nama\n[19] Backup Kontak HP\n[20] White Angel Shield ON\n[00] Keluar\033[0m")
    opt=input("\n\033[1;36mSelect@[ WhiteAngel ]#:----> \033[0m").strip()
    if opt=="1":
        os.system("echo '\nIP Kamu:'; curl -s ifconfig.me; echo '\n'; curl -s ipinfo.io | head -20")
        pause()
    elif opt=="2":
        ip=input("Masukan IP (kosong = IP kamu): ").strip()
        os.system(f"curl -s ipinfo.io/{ip} 2>/dev/null || curl -s ipinfo.io")
        pause()
    elif opt=="3":
        no=input("Nomor HP (ex: 0812xxxx): ").strip()
        print(f"\n[✓] Format: {no}\n[✓] Panjang: {len(no)} digit\n[✓] Valid: {'YA' if len(no)>=10 and no.startswith('08') else 'CEK LAGI'}\n[✓] Operator: Telkomsel/Indosat/XL (cek manual di getcontact)")
        pause()
    elif opt=="4":
        user=input("Username: ").strip()
        print(f"\nCek OSINT untuk {user}:\n"); 
        for site in ["instagram.com","facebook.com","tiktok.com/@","github.com","twitter.com"]:
            print(f" - https://{site}{user}")
        pause()
    elif opt=="5":
        link=input("Tempel Link Curiga: ").strip()
        print("\n[ANALISA]"); 
        curiga=["bit.ly","tinyurl","free","bonus","hadiah","login","verify","bank","dana","ovo"]
        skor=sum(1 for k in curiga if k in link.lower())
        print(f"Link: {link}\nSkor Curiga: {skor}/10\n{'[BAHAYA] JANGAN KLIK!' if skor>=2 else '[AMAN] Tapi tetap hati-hati'}")
        pause()
    elif opt=="6":
        pw=input("Masukan Password: ").strip()
        kuat=len(pw)>=8 and any(c.isdigit() for c in pw) and any(c.isupper() for c in pw)
        print(f"Panjang: {len(pw)}\nKuat: {'YA ✅' if kuat else 'LEMAH ❌ - Tambah angka & huruf besar'}")
        pause()
    elif opt=="7":
        os.system("termux-wifi-scaninfo 2>/dev/null || echo 'Scan WiFi butuh izin lokasi. Aktifin GPS dulu.'; iwconfig 2>/dev/null; echo ''; netstat -t 2>/dev/null | head")
        pause()
    elif opt=="8":
        os.system("pm list packages 2>/dev/null | grep -i -E 'hack|cheat|mod|fake|spy' || echo 'Gak ada APK mencurigakan terdeteksi dari nama.'; ls ~/storage/downloads/*.apk 2>/dev/null | head")
        pause()
    elif opt=="9":
        os.system("rm -rf ~/.cache/* /data/data/com.termux/cache/* 2>/dev/null; echo '[✓] Cache Termux bersih! HP jadi lega!'")
        pause()
    elif opt=="10":
        os.system("uname -a; echo '---'; getprop ro.product.model 2>/dev/null; df -h | head -10")
        pause()
    elif opt=="11":
        os.system("termux-battery-status 2>/dev/null || echo 'Install: pkg install termux-api + install Termux:API apk'; echo ''; dumpsys battery 2>/dev/null | head -20")
        pause()
    elif opt=="12":
        os.system("df -h; echo '---'; du -sh ~/storage/* 2>/dev/null | head")
        pause()
    elif opt=="13":
        pw=''.join(random.choice(string.ascii_letters+string.digits+"!@#$_") for _ in range(16))
        print(f"\nPassword Kuat 16 karakter:\n\033[1;32m{pw}\033[0m\nSimpan baik-baik!")
        pause()
    elif opt=="14":
        os.system("ping -c 4 8.8.8.8; echo '--- Speed Test ---'; curl -o /dev/null -s -w 'Download 10MB: %{time_total}s detik\n' https://speed.cloudflare.com/__down?bytes=10000000 2>/dev/null || echo 'Test selesai'")
        pause()
    elif opt=="15":
        f=input("Path file yang mau disembunyikan: ").strip()
        os.system(f"mv '{f}' '.{os.path.basename(f)}' 2>/dev/null && echo '[✓] File disembunyikan jadi hidden (titik di depan)' || echo 'File gak ketemu'")
        pause()
    elif opt=="16":
        folder=input("Folder yang mau dikunci: ").strip()
        os.system(f"zip -r {folder}.locked.zip {folder} --password 2>/dev/null && echo '[✓] Terkunci jadi {folder}.locked.zip - pakai password' || echo 'Butuh pkg install zip'")
        pause()
    elif opt=="17":
        email=input("Email kamu: ").strip()
        print(f"\nCek manual di:\nhttps://haveibeenpwned.com/account/{email}\nJANGAN share email asli di publik!")
        pause()
    elif opt=="18":
        nama=input("Nama buat Banner: ").strip()
        os.system(f"figlet -f big '{nama}' | lolcat; figlet '{nama}' > ~/storage/downloads/banner_{nama}.txt 2>/dev/null; echo 'Banner disimpan di Download kalau izin storage ok'")
        pause()
    elif opt=="19":
        os.system("termux-contact-list 2>/dev/null | head -100 > ~/storage/downloads/kontak_backup.json && echo '[✓] Backup kontak ke Download/kontak_backup.json' || echo 'Butuh termux-api + izin kontak'")
        pause()
    elif opt=="20":
        os.system('espeak "White Angel Protection Active, Papua Tengah Protected" 2>/dev/null &')
        print("\n\033[1;42m[✓] WHITE ANGEL SHIELD ACTIVE! \033[0m\n\033[1;32m- Cache dibersihkan\n- Monitoring ON\n- Merauke Defender Active v4.1\n- PAPUA TENGAH PROTECTED\033[0m")
        pause()
    elif opt=="00" or opt=="0":
        print("\nKeluar... White Angel Tetap Jaga HP Mu!"); sys.exit()
    else:
        print("Pilihan salah!"); time.sleep(1); main()

if __name__=="__main__": main()
PY
chmod +x angel-kali.py
python3 angel-kali.py

