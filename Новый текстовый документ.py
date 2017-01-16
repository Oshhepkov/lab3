import re
import requests
import time
file=open('res.html', 'w')
file.write('<!DOCTYPE html><html><head><meta charset=UTF-8"></head><body><ul>')
r=requests.get('https://api.meetup.com/2/open_events?&sign=true..,1w&key=4547d1a36616e767f195658726e687e') 
title=re.findall(r'"name":"([\w\ \(\)\:]+)","id":"[\w ]+","time":([\d]+)', r.text)
adr=re.findall(r'"address_1":"([\w\ \.\&]+)"', r.text)
for i in range(7):
    file.write('<li><ul>'+str(i)+'-'+str(i+1))
    for j in range(len(title)):
        if (int(title[j][1])<((i+1)*86400000+time.time()*1000)) and (int(title[j][1])>(i*86400000+time.time()*1000)):
            file.write('<li>' + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(float(title[j][1])/1000))) + '------------' + str(title[j][0]) + '-----------------' + str(adr[j]) + '</li>')
    file.write('</ul></li>')
file.write('</ul></body></html>')
