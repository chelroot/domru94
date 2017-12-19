#! /usr/bin/env python
# coding: utf-8

import os, shutil
from datetime import datetime, timedelta

#dm = datetime.strftime(datetime.now(), "%d.%m")
#dm = datetime.strftime(datetime.now() + timedelta(hours=+5), "%d.%m")

dm = datetime.strftime(datetime.now() + timedelta(days=+1), "%d.%m")
bbb = '/var/www/html/foto/'

for ii in 'vzonov1',  '19-10', '19-23', 'vzonov2', :
    d = str(bbb + ii + '/' + dm )
    os.mkdir(d)
    fil = str(bbb + ii + '/index.html' )
    a2 = open(fil, 'a')
    a2.write('<a href=' + dm + '>' + dm + '</a><br />' + '\n'),
    a2.close()

    fill = str(d + '/index.html' )
    a3 = open(fill, 'a')
    a3.write('<a href=../>Вернуться</a><br />' + '\n'),
    a3.close()

#    print(dm)


