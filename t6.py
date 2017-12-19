#! /usr/bin/env python
# coding: utf-8

import os, shutil
from datetime import datetime, timedelta

dm = datetime.strftime(datetime.now(), "%d.%m")
dmh = datetime.strftime(datetime.now() + timedelta(hours=-1), "%d.%m")
H = datetime.strftime(datetime.now() + timedelta(hours=-1), "%H") # отнимаем час
bbb = '/var/www/html/foto/'
pwd1 = "/home/vova/n2.txt" # временный файл, который потом стирается

def del_empty_dirs(path):    # фунуция удаляет все пустые каталоги
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)

try:
    for ii in 'vzonov1', '19-10', '19-23', 'vzonov2', : #'230820943-1', 'vzonov1', 'vzonov2', :
        a2 = open(pwd1, 'a')
        ff = str('/home/vova/' + ii + '.txt')
        save_file = open(ff, 'w')
        print (ff)
        bb = str(bbb + ii + '/site')
        for d, dirs, files in os.walk(bb):
            for f in files:
                p = os.path.join(d,f) # формирование адреса
                a2.write(p + '\n'),
        a2.close()
        a2 = open(pwd1, 'r').readlines()
        for line in sorted(a2):
            save_file.write(line)
        save_file.close()
        os.remove(pwd1)
except:
  pass

try:
  for ii in  'vzonov1', '19-10', '19-23', 'vzoznov2', :#'230820943-1', 'vzonov1', 'vzonov2', :
    h = str('/var/www/html/foto/' + ii + '/'+ dmh + '/' + H )
    os.mkdir(h)
    ffff = str('/home/vova/' + ii + '.txt')
    f = open(ffff, 'r')
    iii = 1
    for line in f:
         line = line.strip('\n')
         w = str('/var/www/html/foto/' + ii + '/'+ dmh + '/' + H + '/'+ str(iii) + '.jpg')
         shutil.move(line, w)
         iii = int(iii) + 1

    rr = str(bbb + ii + '/site')

    print (rr)
    del_empty_dirs(rr)
    os.remove(ffff)
except:
  pass

