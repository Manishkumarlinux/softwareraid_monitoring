#!/usr/bin/python

import os
import sys
from pymdstat import MdStat
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

fp = open('/opt/raid.txt', 'r')
msg = MIMEText(fp.read())
fp.close()

#Change Email ID accordingly
me = 'email@domain.com'
you = 'email@domain.com'
msg['Subject'] = 'RAID Problem'
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP("localhost",25)
s.ehlo()
raidcmd = "cat /proc/mdstat" + ">" + "/opt/raid.txt"

mds = MdStat()
raid = ['md0', 'md1', 'md2', 'md125']

for i in raid:
    if mds.used(i) == 2:
        print "raid is ok"

    else:
        os.system(raidcmd)
        s.sendmail(me, [you], msg.as_string())
        print 'done!'
        s.quit()   
