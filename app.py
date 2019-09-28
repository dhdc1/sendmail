# -*- coding: utf-8 -*-

import email.message
import smtplib
from email.header import Header
import datetime
from email.mime.text import MIMEText


def send(q, do, place):
    msg = email.message.Message()

    number = ("แจ้งเตือน!!! หมายเลข {}".format(q)).encode('utf-8').decode()
    text = ("อีก 10 คิว จะถึงคิว {} ของท่าน กรุณาไปรอที่บริเวณ".format(do)).encode('utf-8').decode()
    place = place.encode('utf-8').decode()
    body = """  <h1 style='color:blue'>{0}</h1>
                <h2>{1} <u>{2}</u></h2> """.format(number, text, place)
    msg = MIMEText(body, 'html', 'utf-8')

    msg['Subject'] = Header(number, "utf-8")
    msg['From'] = 'alerthosqueue@gmail.com'
    msg['To'] = 'tehnnn@gmail.com'
    msg.add_header('Content-Type', 'text/html')

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.ehlo()
    s.login('alerthosqueue@gmail.com', 'Qazwsxedcr112233')
    r = s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()
    current_time = str(datetime.datetime.now())
    current_time = current_time[:-7]
    print('Send...', current_time)


if __name__ == '__main__':
    send("A107", "ซักประวัติ", "จุดซักประวัติ")
