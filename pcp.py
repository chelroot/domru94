#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, os, shutil, PythonMagick
import subprocess
from datetime import datetime

ffile='/var/log/pureftpd.log'
ddir = '/var/www/html/foto/'


def fun(cam):  #функция, вместо cam попадет имя камеры
    logg = open(ffile, 'r') # открываем лог файл для чтения
    try:
      for line in logg:       # читаем строчки
        if cam in line:      # ищем ключевое слово имя камеры
          ( _, _, _, _, _, _, _,aaa,)=line.split(' ') # находим 8 элемент в строке название файла
      aaa = aaa.strip('\n')   # убираем перевод строки /n оголяя чистое название файла
     # print(aaa)
      a=str(ddir + cam + '.jpg') # формируем название файла в зависимости от имени камеры
      shutil.copyfile(aaa, a)  # копируем
      bbb=str(ddir + cam + 'a.jpg')
      try:
        image = PythonMagick.Image(aaa)
        image.scale("240x")
        image.write(bbb)
      except:
        pass
      logg.close() #закрываем лог файл
    except:
      pass


def fun1(cam):  #функция, вместо cam попадет имя камеры
    logg = open(ffile, 'r') # открываем лог файл для чтения
    try:
      for line in logg:       # читаем строчки
        if cam in line:      # ищем ключевое слово имя камеры
          ( _, _, _, _, _, _, _,aaa,)=line.split(' ') # находим 8 элемент в строке название файла
      aaa = aaa.strip('\n')   # убираем перевод строки /n оголяя чистое название файла
     # print(aaa + '1111')
     # a=str(ddir + cam + '.jpg') # формируем название файла в зависимости от имени камеры
     # shutil.copyfile(aaa, a)  # копируем
      bbb=str(ddir + cam + 'a.jpg')
      try:
        image = PythonMagick.Image(aaa)
        image.scale("240x")
        image.write(bbb)
      except:
        pass
      logg.close() #закрываем лог файл
    except:
      pass


while True:   # цикл
  for iii in range(10):
    for ii in range(4):
      for q in '19-8', '19-9', '19-10', '19-23', '230820943-1', 'vzonov1', 'vzonov2', :
        fun1(q)
        time.sleep(0.4)

    for qq in '19-8', '19-9', '19-10', '19-23', '230820943-1', 'vzonov1', 'vzonov2', :
      fun(qq)
      time.sleep(0.4)

  inf = open(ffile,"w+b") # записываем 0 байт
  inf.close()

#  now = datetime.now()
#  print(str(now) + '\n'),