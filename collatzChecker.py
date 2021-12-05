
print ("░█████╗░░█████╗░██╗░░░░░██╗░░░░░░█████╗░████████╗███████╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░")
print ("██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔══██╗╚══██╔══╝╚════██║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print ("██║░░╚═╝██║░░██║██║░░░░░██║░░░░░███████║░░░██║░░░░░███╔═╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print ("██║░░██╗██║░░██║██║░░░░░██║░░░░░██╔══██║░░░██║░░░██╔══╝░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print ("╚█████╔╝╚█████╔╝███████╗███████╗██║░░██║░░░██║░░░███████╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║")
print ("░╚════╝░░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
print ("by brandon")

CollatzNumber = input ("enter any number from one to infinity")
iteration = 0


def calculateCollatzEven (num0):
    return float (num0) / 2

def calculateColaltzOdd (num1):
    return float (num1) * 3 + 1 


while float(CollatzNumber) > 1:

    if float(CollatzNumber) % 2 == 0:
       CollatzNumber = calculateCollatzEven (CollatzNumber)
       
    
    else:
       CollatzNumber = calculateColaltzOdd (CollatzNumber)
    
    iteration = iteration + 1

    
    print (iteration, float(CollatzNumber))
    
    if iteration >= 62118:
        print ("the amount of steps has been greater than the record amount, I would advise bringing this number to a research team !")


print ("better luck next time this number had a total of " + str(iteration) + " iterations before stoping to 4, 2, 1")






