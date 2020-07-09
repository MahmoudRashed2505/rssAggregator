import feedparser
from datetime import datetime
import os
import shutil
import smtplib

gm = os.environ.get('gm')
gpassword = os.environ.get('gpassword')

print()
with open('url.txt') as file:
    urls = file.readlines()
    os.mkdir('RSS '+str(datetime.date(datetime.now())))
    os.chdir('RSS '+str(datetime.date(datetime.now())))
    for url in urls:
        feed = feedparser.parse(url)
        site = url.split('.')[1]+'.txt'
        print(site)
        files = os.listdir()
        if site not in files:
            f = open(site,'w')
        else:
            f = open(site,'a')
        for entry in feed.entries:
            f.write("Title: {}\nLink: {}\n\n".format(entry['title'],entry['link']))
        f.close()

os.chdir('..')
shutil.move('RSS '+str(datetime.date(datetime.now())),"C:\\Users\\MahmoudHossamEldenIb\\Desktop")

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(gm,gpassword)
    subject = "New RSS Available on Desktop"
    body = "Hey, Check your Desktop for the New RSS"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(gm,"mahmoud.rashed2505@outlook.com",msg)
