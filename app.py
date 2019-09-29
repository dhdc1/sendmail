# -*- coding: utf-8 -*-

import email.message
import smtplib
from email.header import Header
import datetime
from email.mime.text import MIMEText


def send_mail(to, q, do, place, hos):
    msg = email.message.Message()
    hos = hos.encode('utf-8').decode()
    number = ("หมายเลข {}".format(q)).encode('utf-8').decode()
    text = ("อีก 10 คิว จะถึงคิว {} ของท่าน กรุณาไปรอที่บริเวณ".format(do)).encode('utf-8').decode()
    place = place.encode('utf-8').decode()
    body = """  <div style='background-color:skyblue;padding-top:0px;padding-bottom:0px'>                    
                    <h1 style='color:white;background-color:green;padding:5px'>{0}</h1>
                    <center><h2>แจ้งเตือน !!!</h2></center>
                    <center><h1 style='color:blue'>{1}</h1></center>
                    <h2 style ='padding:15px;background-color:red;color:white'>{2} <u>{3}</u></h2> 
                </div> """.format(hos, number, text, place)
    msg = MIMEText(body, 'html', 'utf-8')

    msg['Subject'] = Header(number, "utf-8")
    msg['From'] = 'เแจ้งเตือนคิว{} <alerthosqueue@gmail.com>'.format(hos)
    msg['To'] = str(to)
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
    send_mail("tehnplk@gmail.com", "D109", "รับยา", "ห้องจ่ายยา", "รพ.บางระจัน")
