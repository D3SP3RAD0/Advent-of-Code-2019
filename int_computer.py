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
                sys.exit("HALT")

            #determine number of parameters needed
            param_count = 3
            if opcode == 3 or opcode == 4:
                param_count = 1


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

            if opcode == 1:     #add two parameters
                program[program[i + 3]] = parameter[0] + parameter[1]
                i = i + 4
            elif opcode == 2:   #multiply two parameters
                program[program[i + 3]] = parameter[0] * parameter[1]
                i = i + 4
            elif opcode == 3:   #gain input
                program[program[i + 1]] = int(input("Opcode 3 Input:"))
                i = i + 2
            elif opcode == 4:   #output only parameter
                print(parameter[0])
                i = i + 2
            elif opcode == 99:
                sys.exit("HALT")
            else:
                print("Error reading opcode...")
                return 0
    except Exception as e:
        print(e)

    print("Program reached end of line...")