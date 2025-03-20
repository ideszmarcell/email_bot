import smtplib
from email.mime.text import MIMEText

def kuldes(email_cim, szoveg, smtp_szerver, smtp_port, felado_email, felado_jelszo):
    """E-mail küldése."""
    try:
        msg = MIMEText(szoveg)
        msg['Subject'] = 'Tárgy'  # Itt adhatod meg a tárgyat
        msg['From'] = felado_email
        msg['To'] = email_cim

        with smtplib.SMTP(smtp_szerver, smtp_port) as szerver:
            szerver.starttls()
            szerver.login(felado_email, felado_jelszo)
            szerver.send_message(msg)
        print(f"E-mail sikeresen elküldve: {email_cim}")
    except Exception as e:
        print(f"Hiba történt az e-mail küldésekor: {email_cim}, hiba: {e}")

def email_kuldo(fajlnev, szoveg, smtp_szerver, smtp_port, felado_email, felado_jelszo):
    """E-mail címek beolvasása és e-mailek küldése."""
    try:
        with open(fajlnev, 'r') as fajl:
            for sor in fajl:
                email_cim = sor.strip()
                if email_cim:  # Üres sorok ellenőrzése
                    kuldes(email_cim, szoveg, smtp_szerver, smtp_port, felado_email, felado_jelszo)
    except FileNotFoundError:
        print(f"Hiba: A '{fajlnev}' fájl nem található.")
    except Exception as e:
        print(f"Váratlan hiba történt: {e}")

# Példa használat
fajlnev = 'email_cimek.txt'  # Az e-mail címeket tartalmazó fájl neve
szoveg = 'Ez egy teszt e-mail.'  # Az elküldendő szöveg
smtp_szerver = 'smtp.gmail.com'  # Az SMTP szerver címe (pl. Gmail esetén)
smtp_port = 587  # Az SMTP szerver portja (Gmail esetén 587)
felado_email = 'te_email_cimed@gmail.com'  # A feladó e-mail címe
felado_jelszo = 'a_jelszavad'  # A feladó e-mail jelszava

email_kuldo(fajlnev, szoveg, smtp_szerver, smtp_port, felado_email, felado_jelszo)