from AutomataStack import npda

class AutomataFunctions:
    def checkWord(word):
        if  npda . accepts_input (word): 
            return 'aceptado' 
        else: 
            return 'rechazado'

    def showTransitions(word):
        stepsTransition=[]
        for config in npda.read_input_stepwise(word):
            if config == set():
                break
            ArrayTransition=(list(config))[0]
            ArrayResiduo=ArrayTransition[1]
            steps=str(ArrayTransition[0])
            if steps == 'q2' and ArrayResiduo!='':
                break
            stepsTransition.append(steps)
        return stepsTransition
        
    def showStack(word):
        stepsR=[]
        stackS=''
        for transition in npda.read_input_stepwise(word):
            if transition == set():
                break 
            stepStack = list(transition)
            PDAstack = (stepStack[0])[2]
            stack = PDAstack[0]
            stackS=''
            for steps in stack:
                stackS+=steps
            stepsR.append(stackS)
        return stepsR
