from PyQt5 import QtWidgets,QtGui,uic,QtCore
from time import sleep

class Node:
    def __init__(self,node,moveP1,moveP2,resizeP1,resizeP2,normalCircle,color):
        node = node
        node.move(moveP1,moveP2)
        node.resize(resizeP1, resizeP2)
        node.setAlignment(QtCore.Qt.AlignCenter)
        node.setStyleSheet(self.validationStyle(normalCircle,color))
    
    def validationStyle(self,normalCircle,color):
        if normalCircle == True and color==False:
            return "border: 3px solid black; border-radius: 40px; text-align:center;"
        elif normalCircle == True and color==True:
            return "border: 3px solid black; border-radius: 40px; text-align:center;background:#fff"
        else:
            return "border: 3px solid black; border-radius: 45px;"
    
    def painterNode(node):
        node.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
    
    def painterEdge(state,buscador):
        if state==0:
            buscador.Q0Q0.setIcon(QtGui.QIcon('imagenes/FirstNodoBlancoA.png'))
            buscador.Q0Q0.setIconSize(QtCore.QSize(81,81))
        elif state==2:
            buscador.Q1Q1.setIcon(QtGui.QIcon('imagenes/FirstNodoBlancoA.png'))
            buscador.Q1Q1.setIconSize(QtCore.QSize(81,81))
        elif state==1:
            buscador.Q0Q2.setIcon(QtGui.QIcon('imagenes/FirstTowBlancoAA.png'))
            buscador.Q0Q2.setIconSize(QtCore.QSize(101,31))
        elif state==3:
            buscador.Q1Q2.setIcon(QtGui.QIcon('imagenes/FirstTowBlancoAA.png'))
            buscador.Q1Q2.setIconSize(QtCore.QSize(101,31))
        else:
            pass
        
    def despainterEdge(state,buscador):
        if state==0:
            buscador.Q0Q0.setIcon(QtGui.QIcon('imagenes/FirstNodo.png'))
            buscador.Q0Q0.setIconSize(QtCore.QSize(81,81))
        elif state==2:
            buscador.Q1Q1.setIcon(QtGui.QIcon('imagenes/FirstNodo.png'))
            buscador.Q1Q1.setIconSize(QtCore.QSize(81,81))
        elif state==1:
            buscador.Q0Q2.setIcon(QtGui.QIcon('imagenes/FirsTow.png'))
            buscador.Q0Q2.setIconSize(QtCore.QSize(101,31))
        elif state==3:
            buscador.Q1Q2.setIcon(QtGui.QIcon('imagenes/FirsTow.png'))
            buscador.Q1Q2.setIconSize(QtCore.QSize(101,31))
        else:
            pass
    
    
    def despainterNode(node):
        node.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
        
        
def validationLanguage(numLanguage,buscador):
    words = [['Search','IDIOM','SPANISH','ENGLISH',
              'PORTUGUESE','SPEED','Proyect - Automata', 
              'Automata pushdown | Palindrome', 'Search'],
             ['Buscador','IDIOMA','ESPAÑOL','INGLES','PORTUGUES',
              'VELOCIDADES','Proyecto - Automata',
              'Automata de pila | palindromo', 'Buscar'],
             ['Buscador','IDIOMA','ESPANHOL','INGLÊS','PORTUGUÊS','Rapidez',
               'Projeto - Automata','Autômatos de pilha | palíndromo',
               'Procurar']]
    
    if numLanguage == 2:
        buscador.Buscador.setText(words[0][0])
        buscador.label_3.setText(words[0][1])
        buscador.Spanish.setText(words[0][2])
        buscador.English.setText(words[0][3])
        buscador.English_2.setText(words[0][4])
        buscador.label_4.setText(words[0][5])
        buscador.label.setText(words[0][6])
        buscador.Etiqueta.setText(words[0][7])
        buscador.BotonBuscar.setText(words[0][8])
    elif numLanguage == 1:
        buscador.Buscador.setText(words[1][0])
        buscador.label_3.setText(words[1][1])
        buscador.Spanish.setText(words[1][2])
        buscador.English.setText(words[1][3])
        buscador.English_2.setText(words[1][4])
        buscador.label_4.setText(words[1][5])
        buscador.label.setText(words[1][6])
        buscador.Etiqueta.setText(words[1][7])
        buscador.BotonBuscar.setText(words[1][8])
    elif numLanguage == 3:
        buscador.Buscador.setText(words[2][0])
        buscador.label_3.setText(words[2][1])
        buscador.Spanish.setText(words[2][2])
        buscador.English.setText(words[2][3])
        buscador.English_2.setText(words[2][4])
        buscador.label_4.setText(words[2][5])
        buscador.label.setText(words[2][6])
        buscador.Etiqueta.setText(words[2][7])
        buscador.BotonBuscar.setText(words[2][8])
        