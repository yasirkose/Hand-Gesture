import PyQt5,sys
from PyQt5 import QtGui,QtWidgets,uic,QtCore,Qt
from PyQt5.QtWidgets import *
import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pyautogui import screenshot
import screen_brightness_control as sbc
from PyQt5.QtWidgets import QFileDialog
import os


class anaSayfa(QMainWindow):
    def __init__(self):
        super(anaSayfa, self).__init__()
        uic.loadUi('form.ui', self)
        self.buttonBaslat.clicked.connect(self.programBaslat)
        self.show()

    def programBaslat(self):
        self.dosyaPath = None
        self.sayac = 0
        self.setVisible(False)
        durum=0
        cap = cv2.VideoCapture(0)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        detector = htm.handDetector(detectionCon=0.7)
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
            if durum == 0:
                cv2.putText(img, "Algilama Kapali", (width - 180, height - 20), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (0, 0, 255), 3)
            elif durum == 1:
                cv2.putText(img, "Algilama Acik", (width - 150, height - 20), cv2.FONT_HERSHEY_COMPLEX,
                            0.6, (3, 252, 23), 3)

            if len(lmList) != 0:
                if durum == 0:
                    if ((lmList[8][1] + 20 < lmList[6][1]) and (lmList[12][1] + 20 < lmList[10][1]) and (
                            lmList[16][1] + 20 < lmList[14][1]) and (lmList[20][1] + 20 < lmList[18][1]) and (
                                lmList[4][2] < lmList[2][2]) and (lmList[8][2] < lmList[12][2]) and (
                                lmList[3][2] < lmList[7][2]) and (lmList[1][1] < lmList[5][1]) and (
                                lmList[3][2] < lmList[5][2])) or (
                            (lmList[8][1] > lmList[6][1] + 20) and (lmList[12][1] > lmList[10][1] + 20) and (
                            lmList[16][1] > lmList[14][1] + 20) and (lmList[20][1] > lmList[18][1] + 20) and (
                                    lmList[4][2] < lmList[2][2]) and (lmList[8][2] < lmList[12][2]) and (
                                    lmList[3][2] < lmList[7][2]) and (lmList[1][1] > lmList[5][1]) and (
                                    lmList[3][2] < lmList[5][2])):
                        durum = 1
                elif durum == 1:
                    if ((lmList[8][1] + 20 < lmList[6][1]) and (lmList[12][1] + 20 < lmList[10][1]) and (
                            lmList[16][1] + 20 < lmList[14][1]) and (lmList[20][1] + 20 < lmList[18][1]) and (
                                lmList[4][2] > lmList[2][2]) and (lmList[8][2] > lmList[12][2]) and (
                                lmList[3][2] > lmList[7][2]) and (lmList[1][1] < lmList[5][1]) and (
                                lmList[3][2] > lmList[5][2])) or (
                            (lmList[8][1] > lmList[6][1] + 20) and (lmList[12][1] > lmList[10][1] + 20) and (
                            lmList[16][1] > lmList[14][1] + 20) and (lmList[20][1] > lmList[18][1] + 20) and (
                                    lmList[4][2] > lmList[2][2]) and (lmList[8][2] > lmList[12][2]) and (
                                    lmList[3][2] > lmList[7][2]) and (lmList[1][1] > lmList[5][1]) and (
                                    lmList[3][2] > lmList[5][2])):
                        durum = 0

                    elif ((lmList[8][2] < lmList[7][2]) and (lmList[12][2] > lmList[9][2]) and (
                            lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (
                                  lmList[0][2] > lmList[17][2]) and (
                                  ((lmList[4][1] < lmList[20][1]) and (lmList[4][1] > lmList[8][1])) or (
                                  (lmList[4][1] > lmList[20][1]) and (lmList[4][1] < lmList[8][1]))) and (
                                  lmList[4][2] > lmList[8][2]) and (lmList[4][2] < lmList[1][2])):
                        cv2.putText(img, "Bir", (20, 30), cv2.FONT_HERSHEY_COMPLEX,
                                    0.6, (255, 0, 0), 3)
                        self.parlaklikArttir()

                    elif ((lmList[8][2] < lmList[7][2]) and (lmList[12][2] < lmList[9][2]) and (
                            lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (
                                  lmList[0][2] > lmList[17][2]) and (
                                  ((lmList[4][1] < lmList[20][1]) and (lmList[4][1] > lmList[8][1])) or (
                                  (lmList[4][1] > lmList[20][1]) and (lmList[4][1] < lmList[8][1]))) and (
                                  lmList[4][2] > lmList[12][2]) and (lmList[4][2] < lmList[1][2])):
                        cv2.putText(img, "Iki", (20, 30), cv2.FONT_HERSHEY_COMPLEX,
                                    0.6, (255, 0, 0), 3)
                        self.parlaklikAzalt()
                    elif ((lmList[8][2] < lmList[7][2]) and (lmList[12][2] < lmList[9][2]) and (
                            lmList[16][2] < lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (
                                  lmList[0][2] > lmList[17][2]) and (
                                  ((lmList[4][1] < lmList[20][1]) and (lmList[4][1] > lmList[8][1])) or (
                                  (lmList[4][1] > lmList[20][1]) and (lmList[4][1] < lmList[8][1]))) and (
                                  lmList[4][2] > lmList[16][2]) and (lmList[4][2] < lmList[1][2])):
                        cv2.putText(img, "Uc", (20, 30), cv2.FONT_HERSHEY_COMPLEX,
                                    0.6, (255, 0, 0), 3)
                        self.sesSeviyesiSifirla()
                    elif ((lmList[8][2] < lmList[7][2]) and (lmList[12][2] < lmList[9][2]) and (
                            lmList[16][2] < lmList[13][2]) and (lmList[20][2] < lmList[17][2]) and (
                                  lmList[0][2] > lmList[17][2]) and (
                                  ((lmList[4][1] < lmList[20][1]) and (lmList[4][1] > lmList[8][1])) or (
                                  (lmList[4][1] > lmList[20][1]) and (lmList[4][1] < lmList[8][1]))) and (
                                  lmList[4][2] > lmList[16][2]) and (lmList[4][2] < lmList[1][2])):
                        cv2.putText(img, "Dort", (20, 30), cv2.FONT_HERSHEY_COMPLEX,
                                    0.6, (255, 0, 0), 3)
                        self.sesSeviyesiMaxla()
                    elif ((lmList[8][2] < lmList[5][2]) and (lmList[12][2] < lmList[9][2]) and (
                            lmList[16][2] < lmList[13][2]) and (lmList[20][2] < lmList[17][2]) and (
                                  lmList[4][1] < lmList[8][1]) and (lmList[8][1] < lmList[12][1]) and (
                                  lmList[12][1] < lmList[16][1]) and (lmList[16][1] < lmList[20][1])) or (
                            (lmList[8][2] < lmList[5][2]) and (lmList[12][2] < lmList[9][2]) and (
                            lmList[16][2] < lmList[13][2]) and (lmList[20][2] < lmList[17][2]) and (
                                    lmList[4][1] > lmList[8][1]) and (lmList[8][1] > lmList[12][1]) and (
                                    lmList[12][1] > lmList[16][1]) and (lmList[16][1] > lmList[20][1])):
                        cv2.putText(img, "Bes", (20, 30), cv2.FONT_HERSHEY_COMPLEX,
                                    0.6, (255, 0, 0), 3)
                        self.ekranResmiAl()

            cv2.imshow("Ekran", img)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                quit()
                break

    def ekranResmiAl(self):
        ekranResmi=screenshot()
        #dosyaPath =Null
        if self.dosyaPath==None:
            self.dosyaPath = QFileDialog.getExistingDirectory(caption='Choose Directory', directory=os.getcwd())
            if self.dosyaPath != "":
                path = self.dosyaPath + "/elHareketiyleAlinanSS"+str(self.sayac)+".png"
                self.sayac=self.sayac+1
                ekranResmi.save(path)
        else:
            path = self.dosyaPath + "/elHareketiyleAlinanSS" + str(self.sayac) + ".png"
            self.sayac = self.sayac + 1
            ekranResmi.save(path)

    def parlaklikArttir(self):
        sbc.set_brightness(100)

    def parlaklikAzalt(self):
        sbc.set_brightness(0)

    def sesSeviyesiSifirla(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volRange = volume.GetVolumeRange()
        minVol = volRange[0]
        volume.SetMasterVolumeLevel(minVol, None)

    def sesSeviyesiMaxla(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volRange = volume.GetVolumeRange()
        maxVol = volRange[1]
        volume.SetMasterVolumeLevel(maxVol, None)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = anaSayfa()
    app.exec_()