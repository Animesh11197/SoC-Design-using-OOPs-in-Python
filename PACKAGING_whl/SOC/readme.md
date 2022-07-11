SoC using OOPS




About Different Classes present in the Project:-


1. Instruction Decoder:-
Instruction Decoder inherits the FILE class and takes basically different inputs, which are ADD, SUB, MUL, DIV, LOAD, STORE, IN, OUT. 
It invokes a “checker” function, which will check whether the instruction entered belongs to the set of considered instructions.
Further, we have “read_instruction” which opens a text file and read every instruction in the file, line by line.
We are also handling the exception of getting the wrong instruction in a line here, by displaying the message “Wrong Instruction” for it.


2. Memory:-
In this class, we have created a dictionary “Memory”, which stores the data at the specific addresses, based on the key and value of the dictionary.


3. COMM_BUSSES:-
This class inherits the “Memory” class such that the functions “data_bus” and “address_bus” are able to access the address and data defined in the memory dictionary of the “Memory” Class.


4. ALU:-
The ALU class is a sub-class of the CPU class, where the most basic function implemented in ALU is the logical functions, which are “AND”, “OR”, “NOT”, “XOR”.


5. CPU:-
The CPU class inherits the “Instruction Decoder” class because we need to get the information about the decoded instruction in every line of the file. This is done by invoking the constructor of the parent “Instruction Decoder” class inside the constructor of the “ALU” class.
Along with it, the CPU class also inherits IO and COMM_BUSES class, as it needs to access the methods defined in those classes.
Further, the arithmetic functions like “ADD”, “SUB”, “MUL”, “DIV” are implemented with the help of logical instructions defined in the sub-class ALU. Also, we handled the exception of the divisor being “0” in the DIV function.
Further, the memory operations of reading and writing to the memory is addressed with the help of “LOAD” and “STORE” functions, by invoking the “add_bus” and “data_bus” functions defined inside the “COMM_BUSES” class to access the memory and perform corresponding operations at the relevant addresses.






6. IO:-
IO class inherits FILE class and prints the input of every line from the input file and for every input prints the output accordingly.


7. File:-
File class accepts the input file in which the instructions to be performed is given, and the file handling has also been done in this class. It has two functions: one of them will print the output into a file and another one is reading the inputs from the input file.




INSTRUCTIONS:


ADD-- Adds the given operants
SUB-- Subtracts given operants
MUL-- Multiplies given operants
DIV-- Divides given operants
LOAD-- Loads the value of specific address from MEMORY
STORE-- Stores any value at the defined address
IN-- stores the value from an address to Accumulator of CPU
OUT-- stores the value of Accumulator into a file


ADD, SUB, MUL, DIV instruction needs either of one or two arguments, possible combinations are:
* Data, Data
* Data Address(Data at this address will be fetched)
* Address Data
The arithmetic instructions operate on the arguments passed and operate upon the  
            passed value or value at the address passed as an argument or the variable passed.
LOAD instruction needs one argument which will be a memory address from which we want to load some data.
STORE instruction needs two arguments which one will be data and another one will be memory address so the data will get stored at that particular address.
IN instruction needs one argument, data input from input port
OUT instruction prints the previously performed instruction into the output file.
________________






Format in which Instruction has to be entered in a file:-


        ADD <address or variable or value> <address or variable or value> 
        SUB <address or variable or value> <address or variable or value>
        MUL <address or variable or value> <address or variable or value>
DIV <address or variable or value> <address or variable or value>
        LOAD <address>           //NOTE: Will give an exception if the Address not stored earlier
        STORE <address> <value>
        IN <value>     //Input the value passed with the instruction into the accumulator.
        OUT              // Outputs the present accumulator value in a separate file
 
Note: Either one or two arguments are allowed while performing arithmetic instructions like ADD, SUB, MUL, DIV.