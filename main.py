import requests
import selectorlib
import smtplib, ssl
import time
import sqlite3



URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")


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
    row = scraped.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
    connection.commit()


def read(scraped):
    row = scraped.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",(band, city, date))
    rows = cursor.fetchall()
    return rows



if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        print(scraped)
        
        
        if scraped != "No upcoming tours":
            row = read(scraped)
            if not row:
                store(scraped)
                send_email(message="New event found")
                
        time.sleep(10)