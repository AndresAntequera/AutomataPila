from Nodo import Node
from PyQt5 import QtWidgets
from time import sleep

def wait(time):
    QtWidgets.QApplication.processEvents()
    sleep(time)   

def showTransition(listTransitions,speed,buscador):
    state = 0
    
    for count in range(len(listTransitions)):    
        try:
            if listTransitions[count]=='q0' and listTransitions[count+1]=='q0':
                state=0
                Node.painterNode(buscador.Q0)
                wait(speed)
                Node.despainterNode(buscador.Q0)
                Node.painterEdge(state,buscador)
                wait(speed)
                Node.despainterEdge(state,buscador)
            elif listTransitions[count]=='q0' and listTransitions[count+1]=='q1':
                Node.painterNode(buscador.Q0)
                wait(speed)
                Node.despainterNode(buscador.Q0)
                state=1
                Node.painterEdge(state,buscador)
                wait(speed)
                Node.despainterEdge(state,buscador)
                Node.painterNode(buscador.Q1)
                wait(speed)
                Node.despainterNode(buscador.Q1)
                
            elif listTransitions[count]=='q1' and listTransitions[count+1]=='q1':
                Node.painterNode(buscador.Q1)
                state=2
                Node.painterEdge(state,buscador)
                wait(speed)
                Node.despainterEdge(state,buscador)
                wait(speed)
                Node.despainterNode(buscador.Q1)
                
            elif listTransitions[count]=='q1' and listTransitions[count+1]=='q2':
                state=3
                Node.painterNode(buscador.Q1)
                Node.painterEdge(state,buscador)
                wait(speed)
                Node.despainterNode(buscador.Q1)
                Node.despainterEdge(state,buscador)
                Node.painterNode(buscador.Q2)
                wait(speed)
                Node.despainterNode(buscador.Q2)
            else:
                continue
        except:
            pass
        
def showTransitionStack(list,speed,buscador):
    buscador.pila2.setText('')
    buscador.pila3.setText('')
    buscador.pila4.setText('')
    wait(1)
    state = 0
    for i in range(len(list)):
        try:
            # print(list[i],state)
            if list[i] == '#' and state==0:
                buscador.pila1.setText('#')
                wait(speed)
                state=1
            elif list[i] == '#a' and state==1:
                wait(speed)
                buscador.pila2.setText('a')
                state=2
            elif list[i] == '#b' and state==1:
                wait(speed)
                buscador.pila2.setText('b')
                state=2
            elif list[i] == '#bb' and state==2:
                wait(speed)
                buscador.pila3.setText('b')
                state=3
            elif list[i] == '#ba' and state==2:
                wait(speed)
                buscador.pila3.setText('a')
                state=3 
            elif list[i] == '#ab' and state==2:
                wait(speed)
                buscador.pila3.setText('b')
                state=3
            elif list[i] == '#aa'and state==2:
                wait(speed)
                buscador.pila3.setText('a')
                state=3
            elif (list[i] == '#a' or list[i] == '#b') and state==3:
                wait(speed)
                buscador.pila3.setText('')
                state=2
            elif list[i] == '#' and state==2:
                wait(speed)
                buscador.pila2.setText('')
            else: 
                continue
        except:
            continue
