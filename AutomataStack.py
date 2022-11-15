from automata.pda.npda import NPDA

npda  =  NPDA ( 
    states = {'q0','q1','q2'}, 
    input_symbols = { 'a' , 'b' }, 
    stack_symbols = { '#' , 'a' , 'b' }, 
    transitions = { 
        'q0' :  { 
            'b' : {
                'b': {( 'q0' ,  ( 'b' , 'b' ))},
                'a': {( 'q0' ,  ( 'b' , 'a' ))},
                '#': {( 'q0' ,  ( 'b' , '#' ))},
                'b': {( 'q1' ,  '' ),}
                },  
            'a' : {
                'b': {( 'q0' ,  ( 'a' , 'b' ))},
                'a': {( 'q0' ,  ( 'a' , 'a' ))},
                '#': {( 'q0' ,  ( 'a' , '#' ))},
                'a': {( 'q1' ,  '' )}
            }
        }, 
        'q1' :  { 
            'b' :  { 'b' :  {( 'q1' , '' )}}, 
            'a' :  { 'a' :  {( 'q1' , '' )}}, 
            '' :  { '#' :  {( 'q2' , '#' )}} 
        }
    }, 
    initial_state = 'q0' , 
    initial_stack_symbol = '#' , 
    final_states = { 'q2' }, 
    acceptance_mode = 'final_state' 
)


