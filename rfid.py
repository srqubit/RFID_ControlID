#!/usr/bin/python
# coding=utf-8

import serial

def read_rfid(porta, velocidade):
    try:
        ser = serial.Serial(porta)
        ser.baudrate = int(velocidade)
        daten = str(ser.read(14))
        
        ser.close()    
        daten = daten.replace("\\x02", "" )
        daten = daten.replace("\\x03", "" )
        daten = daten.replace("\\r\\n", "" )
        daten = daten.replace("b'", "" )
        daten = daten.replace("'", "" )
        daten = daten.replace(" ", "" )
        daten = str(hex(int(daten)))
        daten = daten.replace("0x", "" )

        return daten.upper()
    except:
        return 0