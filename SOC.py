'''
-------------------------------------------------THE SoC Design using OOPS----------------------------------------------------------------------------------
                                                    OOPD Monsoon 2021



CLASSES:
File: helps in File Handling
Instructor_Decoder: Helps in decoding the recieved INSTRUCTION from input File
IO: helps display all the results of instructions executed in ALU.
MEMORY: stores all the Addresses, variables and their values.
COMM_BUSSES: includes ADDRESS BUS and the DATA BUS
CPU-- includes [Instruction Decoder|ALU(subclass)|COMM_BUSSES|IO]
ALU- subclass in CPU to perform basic GATES

INSTRUCTIONS:
ADD-- Adds the given operants
SUB-- Substracts given operants
MUL-- Multiplies given operants
DIV-- Divides given operants
LOAD-- Loads the value of specific address from MEMORY
STORE-- Stores any value at the defined address
IN-- stores the value from an address to Accumulator of CPU
OUT-- stores the value of Accumulator into a file


PRINCIPLES USED:


INHERITANCE: 
            > Inheritance has been utilized extensively as we perform: 
            >   Multiple inhertance in CPU class From Instruction Decoder,COMM_BUSSES and IO classes 
            >   inheritance of File class in INSTRUCTION_DECODER
            >   inhertance of Memory class in COMM_BUSSES.

POLYMORPHISUM:
            > METHOD OVERLOADING: Arthematic operations such as ADD,MUL,SUB,DIV can operate with 2 arguments as well as with 1 argument.
            > So, our program would be able to run instructions of both type: ADD <arg1> or ADD <arg1> <arg2>
            > Now, these arguments can also be a direct value, or an address or a variable.

ENCAPSULATION:
            > The methods and data of every component of SoC have been encapsulated seperately in different classes
            > DATA ENCAPSULATION: The data members of every class have been protected whereever required.
            >                     And used getter/setters methods in classes to access or change private class members.

ABSTRACTION: 
            > Used ABC package and decorator @abstractmetod to make our CPU method execute as abstractmethod, thus making CPU as an abstract class.
            > PROCESS ABSTRACTION:        
            > The user just need to provide the name of file where all the INSTRUCTION have been noted, and then the Program produces the corresponding output file.

FILE HANDLING:
            > handling the inputs from any input.txt file from user
            > creating an output file for storing outputs corresponding to every instruction

EXCEPTION HANDLING:
            > used exception handling at appropriate places to tackle the undesired situations or inputs from user
            > implementing using TRY,except and finally blocks.


'''


from abc import ABC, abstractmethod

class File:
  ## File class to handle the input file, which contains the instructions to be executed
  def __init__(self) -> None:
      pass
  
  def print(self,name,instruct,out,mode='a'):
    ## Writes into the output file
    try:
      with open(str(f'{name}') +'.txt', mode) as f:

        f.write('/////////////////////////////////////////////\n')
        f.write(f'INPUT INSTRUCTION :{instruct}\nOUTPUT ----->{out}\n')
      print('OUT:'f'Output Added to File {name}\n\n')
    except:
      print('Writing FILE ERROR.!')

  def read(self,name):
    ## Read from the input file
    try:
      with open(str(f'{name}') +'.txt', 'r') as f:
        read_out=f.readlines()
        #print('Read FILE success.!')
        return read_out
        
    except:
      print('Read ERROR.!!!')

class Instruction_Decoder(File):
  ##Instruction Decoder takes different inputs, which are ADD, SUB, MUL, DIV, LOAD, STORE, IN, OUT. 
  def __init__(self):
    self.__instruction_counter=0  #Encapsulation: Achieved using access specifier , Made the necessary members private to restrict their unintended access > In the current member, it has been made private
    self.error_flag=0
    self.__instruction_set={'ADD':1,'SUB':2,'MUL':3,'DIV':4,'LOAD':5,'STORE':6,'OUT':7,'IN':8} 
    self.out1=0 
    self.out2=0
    self.out3=0
    self.instruction=None  
    
  def get_instructioncounter(self):  # Implemented getter to provide for access to the private member value
    return self.__instruction_counter
  
  def set_instructioncounter(self,value):  # Implemented setter to provide for setting of the private member value
    self.__instruction_counter = value
    
    #self.instruction_error="error: WRONG INSTRUCTION"
  
  def checker(self,input): # what is input parameter
    ## it checks whether the input instruction is a valid instruction or not
    if input in self.__instruction_set:
      return 0
    else:
      return 1
    pass
  
  def Fetch_Decode(self,name):
    ##This function fetches and decode the input instruction from the file, exception handling has also been done
    print('-------------\nINSTRUCTOR DECODER @ instruction',self.__instruction_counter+1)
    try:
      with open(str(name)+'.txt', 'r') as reader:
        read_out=reader.readlines()
        #print("Read_OUT--->",read_out[self.__instruction_counter])
        self.instruction=read_out[self.__instruction_counter]
        inst=self.instruction.split()
        print(inst[0])
        error_flag=self.checker(inst[0])
        if(error_flag==1):
          #print(error_flag)
          raise ValueError("error: WRONG INSTRUCTION")
        else:
          self.out1=inst[0]
          try:
            self.out2=inst[1]
          except:
            pass
          try:
            self.out3=inst[2]
          except:
              self.out3=None
              pass
                
    except ValueError as ve:
      self.out1=0
      self.out2='0'
      self.out3='0'
      print("Wrong Instruction @ line ",self.__instruction_counter+1)
      print(ve)
    
    finally:
      reader.close()
      #print("File Closed")
      if(inst[0]==('LOAD')):
        print('INSTRUCTION DECODER OUTPUTS---',self.out1,self.out2)
      elif(inst[0]==('OUT')):
        print('INSTRUCTION DECODER OUTPUTS---', 'OUT')
      elif(inst[0]==('IN')):
        print('INSTRUCTION DECODER OUTPUTS---',self.out1,self.out2)
      else:
        print('INSTRUCTION DECODER OUTPUTS---',self.out1,self.out2,self.out3)
      self.__instruction_counter+=1
      
        

class IO(File):
  ##IO class which inherits File class and helps us display inputs as well as outputs
  def __init__(self):
    super()._init_()
    self.output=None
    pass
  
  def display(self,instruction=None,output=None):
    ## It prints the outputs of CPU in the desired format at the terminal
    print('-----------------')
    print('CPU:')
    print(f'INPUT INSTRUCTION :{instruction[:-1]}\nOUTPUT ----->{output}')
    File.print(File,'OUTPUTS_File_read',instruction,output)
    print('-----------------\n')
    #print(f'INSTRUCTION:\t{self.}')
    pass

class Memory:
  ##In this class, we have created a dictionary “Memory”, which stores the data at the specific addresses, based on the key and value of the dictionary.
    # will store all the data at specified addresses and variables. 
    Memory={'A':0}
    def set_Accumulator(self,value):
      Memory.Memory['A']=value

   
class COMM_BUSSES(Memory):
  ##COMM_BUSSES class inherits Memory class because it connects our CPU and memory via data bus and address bus
    def __init__(self):
      #super.__init__()
      pass

    def data_bus(self,variable):
      ## This function will print data flowing through the data bus
        #if(self.out1=='STORE'):
        #print('----------------')
        print("data bus initaiated with....",Memory.Memory[variable])

    def add_bus(self,y):
      ## This function will print address fetched from memory on address bus
        #y=self.out2
        print('----------------')
        print('COMM_BUSSES:')
        print("Address Bus initiated: Going to the Memory to find",y)

class CPU(Instruction_Decoder,COMM_BUSSES,IO):
  ## CPU class inherits Instruction_Decoder, COMM_BUSSES, IO classes
  class ALU:
     ##ALU subclass inside CPU class
    def __init__(self) -> None:
        pass
    def AND(self,x,y):
       ## AND operation via this function
      z = x & y
      return z
    def OR(self,x,y):
      ## OR operation via this function
      z=x|y
      return z
    def NOT(self,x):
      ## NOT operation via this function
      z=~x
      return z
    def XOR(self,a,b):
      ## XOR operation via this function
      a1=self.NOT(self,a)
      b1=self.NOT(self,b)
      and1=self.AND(self,a1,b)
      and2=self.AND(self,b1,a)
      xor=self.OR(self,and1,and2)
      return xor
  

  def _init_(self):
    super()._init_()
    self.ALU.__init__(self)
    self.output=None
    pass
## Opertaions below has been done using AND, NOT, OR, XOR functions which are already defined 
  def Add(self,a, b):
    ## ADD operation via this function
    while (b != 0):
        carry = self.ALU.AND(self.ALU,a,b)
        a=self.ALU.XOR(self.ALU,a,b)
        b = carry << 1   
    return a
  
  def subtract(self,x,y):
    ## Subtarction operation via this function
    if(y>x):
        x1=self.ALU.NOT(self.ALU,x)
        sub = y + x1 + 1
        return sub
    else:

        y1=self.ALU.NOT(self.ALU,y)
        sub = x + y1 + 1
        return sub   
  
  def MUL(self,x,y):
    ## Multiplication operation via this function
    z=0
    for i in range(y):
      z=self.Add(z,x)
      i=i+1
    return z
    
  def DIV(self,x,y):
    ## Division operation via this function
    try:
      if (y==0):
        raise ValueError("Can not divide by 0!")     
      else:
        if (x < y):
          return 0
        else:
          z=x
          i=0
          while (z > y-1):
            z=z-y
            i=i+1
          return i
    except ValueError as Ve:
      print(Ve)

  def LOAD(self,variable):
    ## Load the Data from memory 
    try:
      COMM_BUSSES.add_bus(COMM_BUSSES,variable)
      ## Data will go via data bus
      COMM_BUSSES.data_bus(COMM_BUSSES,variable)
      ## Address will be fectched via address bus
      return Memory.Memory[variable]
    except Exception as e:
      print(f'{variable}--NOT previously stored.!')
      return 

  def STORE(self,variable,value):
    ## Store data into memory at a particular address
    #COMM_BUSSES.data_bus(COMM_BUSSES,value)
    COMM_BUSSES.add_bus(COMM_BUSSES,variable)
    Memory.Memory[variable]=value
    print('write success.!')
  
  @abstractmethod    #abstract METHOD of CPU class    
  def execute(self):
    ## This function will check the Input instruction and accordingly produces the output
    if(self.error_flag!=1):
        if(self.out1=='IN'):
            Memory.set_Accumulator(Memory,self.out2)
            self.output=f' Accumulator value set at {self.out2}'
            IO.display(IO,self.instruction,self.output)
        if(self.out1=='OUT'):
            IO.display(IO,self.instruction,self.output)
            File.print(File,'OUTPUT_OUT',self.instruction,self.output,'a')
            return
        #print(not(self.out2.isnumeric()),not(self.out3.isnumeric()))
        if(self.out1=='LOAD'):
            #print('LOAD INSTRUCTION: ',Memory.Memory((self.out2)))
            self.output=self.LOAD(str(self.out2))
            Memory.set_Accumulator(Memory,self.output)
            IO.display(IO,self.instruction,self.output)
            return
        elif(self.out1=='STORE'):
            self.STORE(str(self.out2),(self.out3))
            self.output='STORED Successfully'
            IO.display(IO,self.instruction,self.output)
            #print('STORE INSTRUCTION: ',)
            return
        elif(not(self.out2.isnumeric())):
            try:
                self.out2=self.LOAD(self.out2)
                if self.out2==None:
                  self.output=None
                  IO.display(IO,self.instruction,self.output)
                  return
            except:
                print("variable",self.out2," NOT STORED earlier.!")
        if(not(self.out3)):
            self.out3=Memory.Memory['A']
            #print('Makes sense.!!!!!!!!!!!')
        elif(not(self.out3.isnumeric())):
            try:
                self.out3=self.LOAD(self.out3)
                if self.out3==None:
                  self.output=None
                  IO.display(IO,self.instruction,self.output)
                  return
            except:
                print("variable",self.out3," NOT STORED earlier.!")
        if(self.out1=='ADD'):
            #print('INSTRUCTION :',self.instruction,'OUTPUT----->',self.Add(int(self.out2),int(self.out3)))
            self.output=self.Add(int(self.out2),int(self.out3))
            Memory.set_Accumulator(Memory,self.output)
            IO.display(IO,self.instruction,self.output)
            Memory.set_Accumulator(Memory,self.output)
        elif(self.out1=='SUB'):
            #print('Substraction INSTRUCTION:',self.subtract(int(self.out2),int(self.out3)))
            self.output=self.subtract(int(self.out2),int(self.out3))
            Memory.set_Accumulator(Memory,self.output)
            IO.display(IO,self.instruction,self.output)
        elif(self.out1=='MUL'):
            #print('MUL INSTRUCTION:',self.MUL(int(self.out2),int(self.out3)))
            self.output=self.MUL(int(self.out2),int(self.out3))
            Memory.set_Accumulator(Memory,self.output)
            IO.display(IO,self.instruction,self.output)
        elif(self.out1=='DIV'):
            #print('DIV INSTRUCTION:',self.DIV(int(self.out2),int(self.out3)))
            self.output=self.DIV(int(self.out2),int(self.out3))
            Memory.set_Accumulator(Memory,self.output)
            IO.display(IO,self.instruction,self.output)
    else:
        print('Moving to next instruction........\n')
    
  

# Runs the SoC operations on every File instructions
def RUN(CPU,name='File_read'):
  ## Acts as an interface
  file = open(str(name)+".txt", "r")
  nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
  line_count = len(nonempty_lines)
  file.close()
  print('Lines:',line_count)
  for i in range(line_count):
    CPU.Fetch_Decode(name)
    CPU.execute()
  
  
  

if __name__=='__main__':

  obj=CPU()
  while(True):
    name=input('''
    Welcome To THE SoC: 
    ***************
    To start:
      Enter Input File Name you would like me to Process
    To Exit:
      press f
    ***************
    ''')
    if(name!='f'):
      RUN(obj,name)
      obj.set_instructioncounter(0)
    else:
      print('''
    Ending the session......
    Have a Nice Day
        BYE.!
    ****************************
    ''')
      break
    

    #print('\nMEMORY---->',Memory.Memory)
