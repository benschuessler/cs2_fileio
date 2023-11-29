#Name
#Descrption
#Bugs
#Bonuses
#TestCases:
#Log: 1/1/2023 - Added Main



import csv
import matplotlib.pyplot as plt #program providing graph (boys vs. girls graph)
def main():
   
   
    """ doc """
    file_input = open(r"c:\Users\bschuessler26\Downloads/FileIOData.csv")

    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True

    print("Menu: Enter Choice or 'Q' to (Q)uit:")
    print("1) Print number of Students in Grade 12")
    print("2) Print number of Male Students")
    print("3) Print number of Female Students")
    print("4) Print number of Students in Connecticut")
    print("5) Print number of Students in New York")
    print("6) Enter student's first and last name for student information") 
    print("7) Enter zipcode for number of students in area")
    print("8) Print number of students per zip code")
    print("9) Print graph of males and females")
    print("10) Print all students sorted by last name")
    print("11) Add student information")
   
    while go is True:
        answer = input("Enter Choice or 'Q' to quit")
        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            check_males(file_input)
        elif answer == "3":
            check_females(file_input)
        elif answer == "4":
            check_ct(file_input)
        elif answer == "5":
            check_ny(file_input)
        elif answer == "6":
            check_info(file_input)
        elif answer == "7":
            check_zipcode(file_input)
        elif answer == "8":
            check_ziptally(file_input)
        elif answer == "9":
            graph_students(file_input)
        elif answer == "10":
            check_names(file_input)      
        elif answer == "11":
            check_add_data(file_input)   
        elif answer == "Q":
            go = False
            print("bye")
            return
           



def check_seniors(file_in):
    #Description: checks number of students in 12th grade 
    #Takes column 3 data (grade): kid[3]
    #Returns number of seniors: seniors
    seniors = 0
    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "12":
            seniors += 1
    print(seniors)



def check_males(file_in):
    #Description: checks number of male students in all grades
    #Takes column 4 data (gender): kid[4]
    #Returns number of males: males
    males = 0
    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:
        kid = record.split(",")
        if kid[4] == "M":
            males += 1
    print(males)

def check_females(file_in):
    #Description: chekcs number of female students in all grades
    #Takes clumn 4 data (gender): kid[4]
    #Returns number of females: females
    females = 0
    file_in.seek(1)                                     #move pointer to line 1
    
    for record in file_in:
        kid = record.split(",")
        if kid[4] == "F":
            females += 1
    print(females)

def check_ct(file_in):
    #Description: checks number of students that live in Connecticut
    #Takes column 8 data (State): kid[8]
    #Returns number of students that live in Connecticut: ct
    ct = 0
    file_in.seek(1)

    for record in file_in:
        kid = record.split(",")
        if kid[8] == "CT":
            ct += 1
    print(ct)
        
def check_ny(file_in):
    #Description: checks number of students that live in New York
    #Takes column 8 data (state): kid[8]
    #Returns number of students that live in New York: ny
    ny = 0
    file_in.seek(1)

    for record in file_in:
        kid = record.split(",")
        if kid[8] == "NY":
            ny += 1
    print(ny)


def check_info(file_in):
    #Description: gives students information based on the entered first and last name
    #Takes students first and last name: kid[0], kid[2]
    #returns all of students information: kid
    student = input("enter your students first and last name").split(' ')
    
    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")

        if student[0] == kid [0] and student[1] == kid [2]:
            print(kid)
    else:
         print ("no match")

def check_zipcode(file_in):
    #Description: gives number of students living in entered zipcode
    #Takes entered zip code: zipcode
    #Returns number of students in zipcode: zip_counts
    zipcode = input("enter zipcode for number of students in that area")

    zip_counts = {}

    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")

        if kid[9] in zip_counts.keys():
            zip_counts[kid[9]] += 1
        else:
            zip_counts[kid[9]] = 1
    print(zip_counts[str(int(zipcode))])


def check_ziptally(file_in):
    #Description: Gives list of all possible zip codes and number of students in each zip code
    #Takes column 9 data (zip codes): kid[9]
    #Returns list of zip codes and number of students in each zip code: zip_counts

    zip_counts = {}

    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")

        if kid[9] in zip_counts.keys():
            zip_counts[kid[9]] += 1
        else:
            zip_counts[kid[9]] = 1
    print(zip_counts)

def graph_students(file_in):
    #Description: creates a bar graph of boys, girls, and total students
    #Takes column 4 data (gender): kid[4]
    #Returns bar graph of boys vs. girls: plt.bar, plt.title, plt.show
    boys, girls, total = 0, 0, 0
    file_in.seek(0)
    next(file_in)

    for record in file_in:
        kid = record.split(",")
        total += 1
        if kid[4].strip() == "M":
            boys += 1
        elif kid[4].strip() == "F":
            girls += 1

    labels = ['boys', 'girls', 'Total']
    values = [boys, girls, total]

    plt.bar(labels, values)
    plt.title('Males vs. Females')
    plt.show()

    
def check_names(file_in):
    #Description: prints every student in the school sorted alphabetically by last name
    #Takes Column 2 data (last name): kid[2]
    #Returns list of every students first and last name sorted alphabetically by last name: kid[0], kid[2]
    file_in.seek(1)
    for record in file_in:
        kid = record.split(",")
        print(kid[0], kid[2])

def check_add_data(file_in):
    #Decription: Allows user to enter new student data to data sheet
    #Takes user input (first name, middle name, last name, etc): add_info
    #Returns: void
    add_info = input("Type in the data for a student. Input their first name, middle name, last name, grade, gender (M/F), teacher's first and last name, town, state, zipcode: (seperate all info by commas)")
    add = add_info.split(",")
    f = open(r"c:\Users\bschuessler26\Downloads/FileIOData.csv", "a")
    var_name = csv.writer(f)
    var_name.writerow(add)                                                   
    f.close()

if __name__ == '__main__':
    main()

