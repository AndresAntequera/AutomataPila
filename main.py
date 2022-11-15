import os
from time import sleep

from PyQt5 import QtCore, QtGui, QtMultimedia, QtWidgets, uic
from PyQt5.QtCore import QPropertyAnimation, QTranslator, QUrl
from PyQt5.QtMultimedia import QAudioOutput, QMediaContent, QMediaPlayer

from functionalities import AutomataFunctions as AF
from Nodo import Node, validationLanguage
from transition import showTransition, showTransitionStack
from AudioQt import definicion

accepted = definicion('accepted','audios/accepted.mp3')
denied = definicion('denied','audios/denied.mp3')
acceptedE = definicion('acceptedE','audios/acceptedE.mp3')
acceptedP = definicion('acceptedP','audios/acceptedP.mp3')
deniedE = definicion('deniedE','audios/deniedE.mp3')
deniedP = definicion('deniedP','audios/deniedP.mp3')

app = QtWidgets.QApplication([])
buscador = uic.loadUi("buscador.ui")
            
def SearchWindow():
    buscador.show()

def transportFuntionE():
    validationLanguage(2,buscador)
 
def transportFuntionEs():
    validationLanguage(1,buscador)
    
def transportFuntionP():
    validationLanguage(3,buscador)

def validation():
    if buscador.Radio3.isChecked():
        return 0.2
    elif buscador.Radio1.isChecked():
        return 1.3
    elif buscador.Radio2.isChecked():
        return 0.6
    else:
        return 0.6
    
def clear():
        buscador.pila2.setText('')
        buscador.pila3.setText('')
        buscador.pila4.setText('')
    

def SearchWord():
    clear()
    word = buscador.BuscarPalabra.text().lower()
    velocity = validation()
    showTransition(AF.showTransitions(word),velocity,buscador)
    showTransitionStack(AF.showStack(word),velocity,buscador)
    stateWord = AF.checkWord(word)
    if stateWord == 'aceptado':
        if buscador.BotonBuscar.text() == 'Buscar':
            accepted.play()
        elif buscador.BotonBuscar.text() == 'Search':
            acceptedE.play()
        else:
            acceptedP.play()
    else:
        if buscador.BotonBuscar.text() == 'Buscar':
            denied.play()
        elif buscador.BotonBuscar.text() == 'Search':
            deniedE.play()
        else:
            deniedP.play()
        
   

buscador.BotonBuscar.clicked.connect(SearchWord)
buscador.English.clicked.connect(transportFuntionE)
buscador.Spanish.clicked.connect(transportFuntionEs)
buscador.English_2.clicked.connect(transportFuntionP)

    
nodeQ0 = Node(buscador.Q0,65,90,80,80,True,False)
nodeQ1 = Node(buscador.Q1,275,90,80,80,True,False)
nodeQ2_1 = Node(buscador.Q2,500,90,80,80,True,False)
nodeQ2_2 = Node(buscador.Q2_2,495,85,90,90,False,False)

buscador.show()
app.exec()
