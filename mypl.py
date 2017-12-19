#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, os, os.path, shutil
from datetime import datetime, timedelta
import locale
loc=locale.getlocale()

#изменяем локаль
locale.setlocale(locale.LC_ALL, ('RU','UTF8'))


def modification_date( filename, frm="%Y-%m-%d-%H-%M-%S"):
    """возращает дату модификации файла в формате "Год-Месяц-День", \
    без проверки на существование файла"""
    t = os.path.getmtime( filename )
    return datetime.fromtimestamp(t).strftime( frm )

dm = datetime.strftime(datetime.now(), "%d.%m")
addir = '/var/www/html/foto/'
bddir = '/foto/'
#chas = datetime.strftime(datetime.now(), "%H")
H = datetime.strftime(datetime.now() + timedelta(hours=-1), "%H")
HH = datetime.strftime(datetime.now(), "%H")
for cam in 'vzonov1',  '19-10', '19-23', 'vzonov2', :
    ddir = str('/foto/' + cam + '/' + dm + '/' + H + '/')
    cddir = str(addir + cam + '/' + dm + '/' + H + '/')
    dr = str(addir + cam + '/' + dm + '/')
    ddr = str(addir + cam + '/' + dm + '/' + H + 'p/')
    ddrr = str('ob74' + cam + '/' + dm + '/' + H + 'p/')
    os.mkdir(ddr)
    dir_work = os.listdir(cddir)  #список файлов и директорий в папке 
    nn = len (dir_work)           #получаем количество файлов в директории
    index1 = str(ddr + '1.html')
    indexx = str(ddr + 'index.html')
    ind = str(dr + 'index.html')

    for F in range(nn):
        F +=1
        JPG=str(str(F) + '.jpg')
        FILE=(cddir + JPG)
        FF=str(ddr + str(F) + '.html')
    # +- 1
        fd=F+1
        if fd >= nn:
          fd=nn-1
        fy=F-1
        if fy <= 1:
          fy=1
        ffd=str(str(fd) + '.html')
        ffy=str(str(fy) + '.html')
    #+-10
        fdd=F+10
        if fdd >= nn:
          fdd=nn-1
        fyy=F-10
        if fyy <= 10:
          fyy=1
        ffdd=str(str(fdd) + '.html')
        ffyy=str(str(fyy) + '.html')
    # +-100
        fddd=F+100
        if fddd >= nn:
          fddd=nn-1
        fyyy=F-100
        if fyyy <= 100:
          fyyy=1
        ffddd=str(str(fddd) + '.html')
        ffyyy=str(str(fyyy) + '.html')

#        os.remove(FF)
        a2 = open(FF, 'w')
        a2.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">' +'\n'),
        a2.write('<title>' + JPG + '</title></head><body>' + '\n' + '<center>' + '\n'),
        a2.write('<h2>' + modification_date(FILE, '%d:%m:%Y') + '\n'),
        a2.write('&ensp;&ensp;&ensp;<a href=../' + H + '/' + JPG + '>' + JPG + '</a>&ensp;&ensp;&ensp;&ensp;' + modification_date(FILE, '%H:%M:%S') + '</h2>' + '\n'),
        a2.write('<a href=../' + H + '/' + JPG +' ><img src=../' + H + '/' + JPG + ' alt="11 CHELSI" width="560" ></a>' + '\n'),
        a2.write('<h3><a href=' + ffyyy + '>-100</a>&ensp;&ensp;<a href=' + ffyy + '>-10</a>&ensp;'),
        a2.write('&ensp;<a href=' + ffy + '>Назад -1</a>&ensp;' + '\n'),
        a2.write('- &ensp;<a href=' + ffd + '>Вперед +1</a> &ensp;<a href=' + ffdd + '>+10</a> &ensp;<a href=' + ffddd + '>+100</a>' + '\n'),
        a2.write('<br /><center><br /><a href=../>Вернуться</a><br /></h3></body></html>' + '\n'),
        a2.close()
    shutil.copyfile(index1, indexx)
    a3 = open(ind, 'a')
    a3.write('<a href=' + H + 'p>' + H + '</a><br />' + '\n'),
    a3.close()