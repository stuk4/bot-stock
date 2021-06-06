from django_cron import CronJobBase, Schedule
import datetime
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from bot.settings import EMAIL_HOST_USER

from django.core.mail import send_mail
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'bot.my_cron_job'    # a unique code

    def do(self):
        web_pro = 'https://www.lenovo.com/cl/es/laptops/laptops-legion/legion-5-series/Legion-5-Pro-16ACH6H/p/88GMY501578'
        web_test = 'https://www.lenovo.com/cl/es/laptops/thinkpad/serie-t/ThinkPad-T15-G1/p/22TPT15T5N1'
        req = Request(web_test, headers={'User-Agent': 'Mozilla/5.0'})
        datos = urlopen(req).read()
        soup =  BeautifulSoup(datos,'html.parser')
        result = soup.find_all("span", {"class": "stock_message"})
        date_now = "{:%d-%m-%Y-%H:%M:%S}".format(datetime.datetime.now())
    
        if len(result[0].text) == 0:
            subject = "BOT VERIFICADOR DE STOCK LENOVO {}".format(date_now)
            message = 'HAY STOOCK MIRA {}'.format(web_pro)
            print("hay stock")
            send_mail(subject, 
                message, EMAIL_HOST_USER, ['bastididierr@gmail.com'], fail_silently = False)
      
        