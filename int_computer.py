import sys

def run(program):
    i = 0
    try:
        while i < len(program):
            instruction = list(map(int, str(program[i])))   #create integer list from instruction
            
            #determine opcode
            if len(instruction) > 1:
                opcode = int(str(instruction[-2]) + str(instruction[-1]))
            else:
                opcode = instruction[-1]

            #halt if done
            if opcode == 99:
                print("HALT")
                return(0)

            #determine number of parameters needed
            param_count = 3
            if opcode == 3 or opcode == 4:
                param_count = 1
            if opcode == 5 or opcode == 6:
                param_count = 2


            while len(instruction) < param_count + 2:  #set default parameter as 0
                instruction.insert(0, 0)

            
            parameter = []                                  #stores values of parameters
            parametermodes = instruction[:-2]
            parametermodes = parametermodes[::-1]

            try:
                for j, digit in enumerate(parametermodes):  #loop that excludes opcode
                    value = program[i + 1 + j]      #set value of position specified
                    #determine parameter for each paramater
                    if digit == 0:          #parameter mode 0, reads from position
                        parameter.append(program[value]) #current index plus 1 plus position of paramter, starting with next parameter
                    elif digit == 1:
                        parameter.append(value)

            except Exception as e:
                print("Error when determining parameters:", e)

            #add two parameters
            if opcode == 1:     
                program[program[i + 3]] = parameter[0] + parameter[1]
                i = i + 4

            #multiply two parameters
            elif opcode == 2:   
                program[program[i + 3]] = parameter[0] * parameter[1]
                i = i + 4

            #gain input
            elif opcode == 3:   
                program[program[i + 1]] = int(input("Input:"))
                i = i + 2

            #output only parameter
            elif opcode == 4:   
                print(parameter[0])
                i = i + 2

            #if first parameter != 0, set pointer to value of second parameter    
            elif opcode == 5:   
                if parameter[0] != 0:
                    i = parameter[1]
                else:
                    i = i + 3

            #if first paramater == 0 set pointer to value of second parameter        
            elif opcode == 6:   
                if parameter[0] == 0:
                    i = parameter[1]
                else:
                    i = i + 3

            #if first parameter is < second parameter, store 1 in the location directed by third parameter        
            elif opcode == 7:   
                if parameter[0] < parameter[1]:
                    store = 1
                else:
                    store = 0
                program[program[i + 3]] = store
                i = i + 4

            #if the first parameter is equal to the second, store one, otherwise 0
            elif opcode == 8:   
                if parameter[0] == parameter[1]:
                    store = 1
                else:
                    store = 0
                program[program[i + 3]] = store 
                i = i + 4
            else:
                print("Error reading opcode...")
                return 0
    except Exception as e:
        print(e)

    print("Program reached end of line...")