#!/usr/bin/python
# coding=utf-8
from threading import Timer
import argparse
import binascii
import serial

def read_rfid(porta, velocidade):
    try:
        ser = serial.Serial(porta)
        ser.baudrate = int(velocidade)
        ser.timeout=10
        ser.flushInput()
        
        daten = ser.readline().strip()
        ser.close()        
        
        hexo = str(daten)
        
        if str(hexo)=="b''":
            return ""
        
        daten = '{:0>8}'.format(hexo.upper())
        daten = daten.replace("B'\\X02", "" )
        daten = daten.replace("'", "" )
        daten = str(hex(int(daten)))
        daten = daten.replace("0x", "" )
        
        return "3C" + '{:0>8}'.format(daten.upper())
    except Exception as e:
        print("Erro leitura RFID " + str(e))
        return ""
