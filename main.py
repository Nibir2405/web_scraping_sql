import requests
import selectorlib
import smtplib, ssl
import time


URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the url and header tell the server that it was a browser"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted_data = extractor.extract(source)
    return extracted_data["tours"]

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "navidulislam2002@gmail.com"
    password = "syahnczbyspsbeam"

    receiver = "nibirislam56@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent")



def store(scraped):
    with open("data.txt", "a") as file:
        file.write(scraped + "\n")

def read(scraped):
    with open("data.txt", "r") as file:
        return file.read()
   

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        print(scraped)
        
        content = read(scraped)
        if scraped != "No upcoming tours":
            if scraped not in content:
                store(scraped)
                send_email(message="New event found")
                print("Email sent")
        time.sleep(10)