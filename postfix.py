# -*- coding: utf-8 -*-
class Stack:
    def __init__(self, itemlist=[ ] ):
        self.items=itemlist     

    def isEmpty(self) :
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)     
        return 0 

    def pop(self):
        return self.items.pop( )  

    def peek(self):                        # same as pop, only doesnt modify the  stack
        return self.items[-1:][0]


def infixtopostfix(infixexpr):
    import re
    
    stack =Stack( )
    postfix = [ ]  
    prec = { '(' : 1 ,  '+' : 2, '-' : 2, '*' : 3, '/' :3,  }   # operator precedance   (    >   ^   >  + - >  *  /     

    #tokenList = infixexpr.split( )                  #create a comma separated list of tokens from the Infix Expression passed  
    tokenList =  re.split("([()+-/* ])", infixexpr.replace(" ", ""))    
    # split the list of tokens with delimiters as any mathematical operator...split( ) doesnt take mor ethan one delimiter
    #print "Split tokenList :",tokenList       #eg :  infix expression A * B + C * D"  gives tokenList  ['A', '*', 'B', '+', 'C', '*', 'D']  
    
    for token in tokenList:      
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' or token in '0123456789'  : 
            postfix.append(token)            # Algo : lf Entered Character is Alphabet or Digit, Print Alphabet as Output
        
        elif token == '(':                              # Algo : If Entered Character is Opening Bracket then Push ‘(‘ Onto Stack
            stack.push(token)  

        elif token == ')':
            topToken=stack.pop()             #  Algo : If Corresponding ‘)’ bracket appears then Start Removing Elements 
            while topToken !=  '(' :               #  Algo : If any Operator Appears before ‘)’ then Push it onto Stack. 
                postfix.append(topToken)
                topToken=stack.pop( )        # Algo : Pop from Stack till ‘(‘ is removed

        else :
            while (not stack.isEmpty( )) and ( prec[stack.peek( )] >= prec[token]) :   
                #Check Whether There is any Operator Already present in Stack
                # If Present check Whether Priority of Incoming Operator is greater than Priority of Topmost Stack Operator

                postfix.append(stack.pop( ))      #Algo :  If  not present on Stack then Push Operator Onto Stack.

            stack.push(token)                              # Algo : If Priority of Incoming Operator is Greater , then  Push Incoming Operator Onto Stack.

    while not stack.isEmpty( ):                      #Algo : Else Pop Operator From Stack again repeat steps
        opToken=stack.pop()
        postfix.append(opToken)
    return postfix


# Function to evaluate Post Fix expression
def evalPostfix(infixexpr) : 
    stack =Stack( )
    tokenList = infixexpr.split( )                  #create a comma separated list of tokens from the Infix Expression passed  
    #print "Split tokenList :",tokenList       #eg :  infix expression A * B + C * D"  gives tokenList  ['A', '*', 'B', '+', 'C', '*', 'D']  
    
    for token in tokenList:      
        if token in "0123456789" :            
            stack.push(int(token))          #Algo : If the token is an operand, convert it from a string to an integer and push the value onto stack
        
        else  :                                             #Algo : If token is an operator, pop two next operands, and perform the operations
            operand2 = stack.pop( )
            operand1 = stack.pop( )
            result = evaluate(token, operand1, operand2)            # Perform the operation
            stack.push(result)                                                                  # Push the result back on the stack.

    return stack.pop( )
         
#Calculation function for different opeartors
def evaluate(operator, operand1, operand2 ) :
    if operator == '+' :
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
 


 #Printing the Menu   
print ""
print ""
print ""
print ""
menu = {}
menu['1']="What are infix postfix and prefix notations?" 
menu['2']="Infix to Postfix Expression Conversion"
menu['3']="Evaluation of Postfix expression"
menu['4']="Exit"

while True:
    options=menu.keys()
    options.sort()
    print""
    print "                  MENU"
    print"============================================="
    for entry in options: 
      print entry, menu[entry]
    print""
    selection=raw_input("Please Select:")
    print""
    print ""

    if selection =='1':
        print "Infix notation       : X + Y     -     Operators are written in-between their operands. "
        print "Postfix notation     : X Y +     -     Operators are written after their operands. "
        print "Prefix notation      : + X Y     -     Operators are written before their operands. "
        print ""
        print ""

    elif selection == '2' : 
        print ""
        print ""
        print ""
        print "              Infix to Postfix Convertor"
        print "              ------------------------------------"
        print "              Enter  your In-Fix  expression to be converted   "
        infix = raw_input( "              Example of In-Fix exprtession could be  (2 + 3) - 7 / 9   :")
        print "              ----------------------------------------------------------"
        postfix = infixtopostfix(infix)

        print ""
        print "              Post Fix expression of   ",infix, "  is   :  "+' '.join(postfix)       #to convert list into string
        print ""
        print ""
        print ""
        choice = raw_input("              Do you want to evaluate the value of your Post Fix expression (Y/N)   :  ")
        if choice == 'Y' or 'y' :
            result = evalPostfix(' '.join(postfix))
            print "              Value of Post Fix expression     is   :",result 
            print "              ----------------------------------------------------------------------------"
            print ""
            print ""
        else :
            continue

    elif selection == '3' : 
        print ""
        print ""
        print ""
        print "              Postfix Value Convertor"
        print "              ------------------------------------"
        print "               Enter  your Post-Fix  expression to be converted   "
        postfix = raw_input( "               Example of Post-Fix exprtession could be  2 3 + 7 9 / -   :")
        print "              ----------------------------------------------------------------------------"
        result = evalPostfix(' '.join(postfix))

        #print "Value of Post Fix expression    ",postfix,"   is   :"+' '.join(result) 
        print "              Value of Post Fix expression     is   :",result 
        print " "
        print ""

    elif selection == '4': 
      break
    else: 
      print "Unknown Option Selected!" 
      print "--------------------------"
      print ""
      print ""
      print ""