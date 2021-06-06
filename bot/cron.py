from django_cron import CronJobBase, Schedule
import datetime
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'bot.my_cron_job'    # a unique code

    def do(self):
        web_pro = 'https://www.lenovo.com/cl/es/laptops/laptops-legion/legion-5-series/Legion-5-Pro-16ACH6H/p/88GMY501578'
        web_test = 'https://www.lenovo.com/cl/es/laptops/laptops-legion/legion-7-series/Lenovo-Legion-7/p/88GMY701410'
        req = Request(web_test, headers={'User-Agent': 'Mozilla/5.0'})
        datos = urlopen(req).read()
        soup =  BeautifulSoup(datos,'html.parser')
        result = soup.find_all("span", {"class": "stock_message"})
        
        print(result[0].text)
        # title = soup.find("meta",  property="og:title")
        # if title:
        #     texto = title["content"] +' '+ ''.join(str(tag.text) for tag in tags)
        # else:
        #     texto = ''.join(str(tag.text) for tag in tags)
      
        print("hola",str(datetime.datetime.now()))