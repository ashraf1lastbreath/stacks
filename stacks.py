class Stack:

    def isEmpty(self) :
        return (self.items==[ ])

    def size(self):
         return len(self.items)

    def __init__(self):
        self.items=[ ]      #initialize to set list to empty list

    def push(self, item):
        self.items.append(item)   #append the item to the list


    def pop(self):
        return self.items.pop( )  #recursive call homonymous method

    def display(self):
        print "             Stack elements :" 
        print"             -------------------------"
        if self.isEmpty( ) :
            print "             Stack is Empty"
        else :
            print "             ",self.items
            print ""
            size = self.size( )
            print "             Size of Stack :", size



stack = Stack( )

menu = {}
menu['1']="Push" 
menu['2']="Pop"
menu['3']="Print Stack"
menu['4']="isEmpty"
menu['5']="Exit"

while True:
    options=menu.keys()
    options.sort()
    print""
    print "        MENU"
    print"======================"
    for entry in options: 
      print entry, menu[entry]
    print""
    selection=raw_input("Please Select:")
    print""
    print ""

    if selection =='1':
        print "              Push element" 
        print"              ---------------------"
        length=input("              Enter the number of items you want on your Stack :   ")
        for counter  in range(1,length+1) :
            item=raw_input("              Enter the Stack element : ")
            stack.push(item)
        print " "
        stack.display( )
       

    elif selection == '2' : 
      print "              Pop  element"
      print "              --------------------"
      stack.pop( )
      stack.display( )
    

    elif selection == '3' :
      print "             Printing  stack"
      print "             --------------------"
      stack.display( )


    elif selection == '4' : 
      print "              Check if Stack is Empty"
      print "              -----------------------------------"
      check=stack.isEmpty()
      if str(check)  == 'True':
        print "              Stack is empty"
      else:
        print "              Stack is NOT empty"

    elif selection == '5': 
      break
    else: 
      print "Unknown Option Selected!" 

