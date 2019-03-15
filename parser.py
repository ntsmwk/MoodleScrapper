from lxml import html
import requests
import csv
import datetime



url = 'https://moodle.jku.at/jku2015/mod/assign/view.php?id=2194989'
cookies = dict(MoodleSessionjku2015SessionCookie='ehr876dtbaeflp4qmdo623m5s1')

page = requests.get(url, cookies=cookies)
parser = html.HTMLParser();

root = html.fromstring(page.content, parser=parser)

participants = root.xpath("//div[@id='page']//tbody/tr[2]/td[2]/text()")[0]
handIn = root.xpath("//div[@id='page']//tbody/tr[3]/td[2]/text()")[0]

with open('data.csv', mode='a+') as data_file:
    data_writer = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow([datetime.datetime.now(), participants, handIn])

