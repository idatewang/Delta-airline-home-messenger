from lxml import html
from lxml.etree import tostring
import requests
from twilio.rest import Client
import time

account_sid = 'Insert account_sid here'
auth_token = 'Insert auth_token here'
client = Client(account_sid, auth_token)
url = "https://news.delta.com/where-delta-flying-june-updated"
count = 0

def call():
    client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='insert number to call',
        from_='insert number to make the call'
    )
    print("called")


web = requests.get(url, timeout=10)
doc = html.fromstring(web.content)

# tracks three airlines to China: from Detroit through Seoul; from Detroit to ShangHai; From Seattle to Seoul
detroit_seoul = doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/ul[6]/li[1]/p")[0]
detroit_seoul = tostring(detroit_seoul)
detroit_shang = doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/ul[6]/li[2]/p")[0]
detroit_shang = tostring(detroit_shang)
seattle_seoul = doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/ul[6]/li[3]/p")[0]
seattle_seoul = tostring(seattle_seoul)

# tracks China-America policy updates
notice = doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/p[12]")[0]
notice = tostring(notice)

start_time = time.time()
while 1:
    while 1:
        try:
            web = requests.get(url, timeout=10)
            break
        except Exception:
            time.sleep(0.1)
            print("Error")
    doc = html.fromstring(web.content)
    detroit_seoul_latest, detroit_shang_latest, seattle_seoul_latest, seattle_shang_latest, notice_latest = "", "", "", "", ""
    while 1:
        try:
            detroit_seoul_latest = tostring(doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/ul[6]/li[1]/p")[0])
            break
        except IndexError:
            time.sleep(0.1)
            with open("log.txt","a") as file:
                print("Error getting detroit_seoul_latest. Last known value is:", detroit_seoul_latest, "\nRetrying...")
                file.write(time.strftime("%H:%M:%S", time.localtime())+"\nError getting detroit_seoul_latest. Last known value is: "+detroit_seoul_latest)
    if detroit_seoul != detroit_seoul_latest:
        print("Original: ", detroit_seoul, "New: ", detroit_seoul_latest)
        call()
        break

    while 1:
        try:
            detroit_shang_latest = tostring(doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/ul[6]/li[2]/p")[0])
            break
        except IndexError:
            time.sleep(0.1)
            with open("log.txt","a") as file:
                print("Error getting detroit_shang_latest. Last known value is:", detroit_shang_latest, "\nRetrying...")
                file.write(time.strftime("%H:%M:%S", time.localtime())+"\nError getting detroit_shang_latest. Last known value is: "+detroit_shang_latest)
    if detroit_shang != detroit_shang_latest:
        print("Original: ", detroit_shang, "New: ", detroit_shang_latest)
        call()
        break

    while 1:
        try:
            seattle_seoul_latest = tostring(doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/ul[6]/li[3]/p")[0])
            break
        except IndexError:
            time.sleep(0.1)
            with open("log.txt","a") as file:
                print("Error getting seattle_seoul_latest. Last known value is:", seattle_seoul_latest, "\nRetrying...")
                file.write(time.strftime("%H:%M:%S", time.localtime())+"\nError getting seattle_seoul_latest. Last known value is: "+seattle_seoul_latest)
    if seattle_seoul != seattle_seoul_latest:
        print("Original: ", seattle_seoul, "New: ", seattle_seoul_latest)
        call()
        break


    while 1:
        try:
            notice_latest = tostring(doc.xpath("//*[@id=\"block-dnh-content\"]/div/div/div/div[1]/p[12]")[0])
            break
        except IndexError:
            time.sleep(0.1)
            with open("log.txt","a") as file:
                print("Error getting notice_latest. Last known value is:", notice_latest, "\nRetrying...")
                file.write(time.strftime("%H:%M:%S", time.localtime())+"\nError getting notice_latest. Last known value is: "+notice_latest)
    if notice != notice_latest:
        print("Original: ", notice, "New: ", notice_latest)
        call()
        break

    current = time.strftime("%H:%M:%S", time.localtime())
    # prints record time
    print(current, "--- %s seconds ---" % (time.time() - start_time))
