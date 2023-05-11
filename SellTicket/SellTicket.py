import sys

#reading and writing
def read_input():
    with open(sys.argv[1], "r") as inputs_file:
        input_lines = inputs_file.read().splitlines()
    return input_lines

def write_output(output_lines):
    with open("output.txt", "w") as outputs_file:
        outputs_file.writelines(output_lines)

l=[]

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def CREATECATEGORY(t,w,h):#t is category name, w and h are integers that create the category
    m=[["X" for x in range(int(w))] for y in range(int(h))]
    m.insert(0,t) #I add the name of the category to the list because I will use the first index of the list to check the name of categories
    l.append(m)

    return "The category '{}' having {} seats has been created".format(t, int(w) * int(h))



def BALANCE(a):
    s_count = 0
    f_count = 0
    t_count = 0
    for category in l:
        if a == category[0]:
            for row in category:
                for letter in row:
                    if letter == "S": 
                        s_count += 1    #calculates the sum of student tickets
                    elif letter == "F": 
                        f_count += 1    #calculates the sum of full tickets
                    elif letter == "T":
                        t_count += 1    #calculates the sum of season tickets
    return "Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars".format(s_count,f_count,t_count,(10*s_count + 20*f_count + 250*t_count))
 

   
def getIndex(category, letter): #splits alphabet with the function "split_alphabet" and sorts for the function "SHOWCATEGORY"
    line_count = len(category)-1
    splited_alphabet = split_alphabet(line_count)
    splited_alphabet.reverse()
    return splited_alphabet.index(letter)

def returnTickets(ticketRange): #this function helps me adapt the ranged type inputs on my functions
    xLetter = ticketRange[:1]
    yLetterList = ticketRange[1:].split("-")
    count = int(yLetterList[1]) - int(yLetterList[0])
    returningList = []
    returningList.append(xLetter + yLetterList[0])
    for y in range(count):
        returningList.append(xLetter + str(y + 1 + int(yLetterList[0])))
    return returningList

def SELLTICKET(a, b, z, ticket_list): # a is the name , b is the type og the customer. z is the category that the customer wants to buy.
    tickets = ""
    for i in ticket_list:
        tickets += (i + " ")
    for ticket in ticket_list:
        if "-" in ticket:
            ticket_list += returnTickets(ticket)
            continue
        

        xLetter = ticket[:1]
        y = ticket[1:]

        if b == "student":
            for category in l:
                x = getIndex(category, xLetter)+1
                if category[0]==z:
                    category[int(x)][int(y)]="S"
        elif b == "full":
            for category in l:
                x = getIndex(category, xLetter)+1
                if category[0]==z:
                    category[int(x)][int(y)]="F"
        elif b == "season":
            for category in l:
                x = getIndex(category, xLetter)+1
                if category[0]==z:
                    category[int(x)][int(y)]="T"
        else:
            print("There is not a tariff like you have entered.")
    return "Success: {} has bought {} at {}".format(a, tickets, z)

  



def CANCELTICKET(z,ticket): #z is the name of the category
    xLetter = ticket[:1]
    y = ticket[1:]

    for category in l:
        x = getIndex(category, xLetter)+1

        if category[0] == z:
            category[int(x)][int(y)]="X"

    return "Success: The seat {} at {} has been canceled and now ready to sell again".format(ticket, z) #buna dön unutma


def split_alphabet(count):
    return alphabet[:count]


def SHOWCATEGORY(a):
    cat_output = ""
    row_count = 0
    for category in l:
        if category[0] == a: #checking the name of the category
                line_count = len(category)-1
                splited_alphabet = split_alphabet(line_count)
                splited_alphabet.reverse()
                for idx, row in enumerate(category):
                    if row == category[0]:
                        continue
                    row_count = len(row)
                    cat_output += splited_alphabet[idx-1] + " "
                    for k in range(len(row)):
                        cat_output += row[k] + "  "
                    cat_output += "\n"
    for column in range(row_count):
        if column >= 10:
            cat_output += " " + str(column)
        else:
            cat_output += "  " + str(column)
    return "Printing category layout of {}".format(a) + "\n\n" + cat_output + "\n" + "category report of '{}'".format(a) + "\n" + "-------------------------------"

def command_checker(line1):

    input_strings = line1.split(" ")
    command = input_strings[0]

    if command == "CREATECATEGORY":
        cat_size = input_strings[2].split("x")
        return CREATECATEGORY(input_strings[1],cat_size[0],cat_size[1])
    elif command == "SELLTICKET":
        using_strings = input_strings[4:]
        return SELLTICKET(input_strings[1],input_strings[2],input_strings[3],using_strings)
    elif command == "CANCELTICKET":
        return CANCELTICKET(input_strings[1],input_strings[2])
    elif command == "SHOWCATEGORY":        
        return SHOWCATEGORY(input_strings[1])
    elif command == "BALANCE":
        return BALANCE(input_strings[1])




input_file_lines = read_input()
output_file_lines = ""

for input_line in input_file_lines:
    output_file_lines += command_checker(input_line) + "\n"
    
write_output(output_file_lines)