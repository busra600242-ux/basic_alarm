import time
from datetime import datetime

def alarm_kur():
    while True:
        alarm = input("Alarm saatini giriniz⏰ (SS:DD, Örn: 20:27) : ").strip()
        cevap = input(f"Alarmınızı doğruluyor musunuz, Alarm saatiniz: {alarm} (evet/hayır) : ")
        cevap = cevap.strip().lower()

        if cevap == "evet":
            print(f"Alarm {alarm} için kuruldu, bekleniyor...")
            while True:
                saat = datetime.now().strftime("%H:%M")
                if saat == alarm:
                    print("ALARM!!⏰")
                    time.sleep(1)
                    break
                time.sleep(1)
            break

        elif cevap == "hayır":
            print("Alarm iptal edildi.")
            cevap2 = input("Alarmı tekrar kurmak ister misiniz (evet/hayır) : ").strip().lower()
            if cevap2 == "evet":
                continue
            elif cevap2 == "hayır":
                print("Kapatılıyor...")
                time.sleep(1)
                break
            else:
                print("Lütfen geçerli bir cevap giriniz.")
                continue

        elif cevap == "":
            print("Kapatılıyor...")
            time.sleep(1)
            break

        else:
            print("Lütfen geçerli bir cevap giriniz.")
            time.sleep(1)

alarm_kur()
