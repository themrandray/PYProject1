import requests
import bs4
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config 

def get_car_data():
    url = "https://www.ss.com/lv/transport/cars/today/" #norade uz sludinājumu servisu
    saturs = requests.get(url)

    if saturs.status_code == 200: #pārbaude vai lapa strādā
        lapa = bs4.BeautifulSoup(saturs.content, "html.parser")
        atrada = lapa.find_all(class_="msga2-o pp6") #šī klase satur auto informaciju
        return atrada
    else:
        print("Lapas ielādes kļūda.")
        return None
    
def print_car_info(car_data):
    for ad in car_data:
        print(ad.text)

def save_to_html(content):
    with open("website.html", "w", encoding='utf-8', errors='ignore') as file:
        file.write(str(content))

def find_new_ads(current_ads, previous_ads):
    if previous_ads is None:
        return current_ads

    new_ads = [ad for ad in current_ads if ad not in previous_ads]
    return new_ads

def send_email(subject, body):
    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = config.USERNAME
    message['To'] = config.SENDTO
    message['Cc'] = config.USERNAME

    html_part = MIMEText(body, "html")
    message.attach(html_part)

    smtp = smtplib.SMTP(config.HOST, config.PORT)
    smtp.starttls()
    smtp.login(config.USERNAME, config.PASSWORD)
    smtp.sendmail(config.USERNAME, config.SENDTO, message.as_string())
    smtp.quit()
    
def main():
    previous_ads = []

    while True:
        current_ads = get_car_data()

        if current_ads:
            if previous_ads:
                new_ads = find_new_ads(current_ads, previous_ads)

                if new_ads:
                    print("Atrasts jauna auto sludinājums:")
                    print_car_info(new_ads)

                    # Sūta epastu ar jauno slūdinājumu
                    email_subject = "Jaunu auto sludinājumi"
                    email_body = "<br>".join(ad.text for ad in new_ads)
                    send_email(email_subject, email_body)

            save_to_html(current_ads)

            time.sleep(30)

            previous_ads = current_ads

if __name__ == "__main__":
    main()