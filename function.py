# user_in=(input("write an input: "))
# print(len(user_in))

# a = "hi, i9ts $ $99.99"
# print(a.count("$"))

# age =21

# if (age>= 18):
#     print("can vote and apply for th license")
    
# elif (age<= 18):
#     print("you're not able to apply ")
def main():
    marks=()
    while True:
        print("###############################################")
        print("## 1- marks >= 90,       Grade = 'A'         ##")
        print("## 2- 90 > marks >= 90,  Grade = 'B'         ##")
        print("## 3- 80 > marks >= 70,  Grade = 'C'         ##")
        print("## 4- 70 > marks >= 60   Grade = 'D'         ##")
        print("## 5- marks <=60 ,       Grade = 'F'         ##")
        print("###############################################")

        marks=int(input("enter the marks of student : "))

        if (marks>=90):
            print("GRADE= 'A' ^_^ ")
        elif(marks >= 80 and marks < 90):
            print("GRADE = 'B' @_@ ")
        elif(marks >= 70 and marks <80 ):
            print("GRADE = 'C' *_* ")
        elif(marks >= 60 and marks < 70):
            print("GRADE = 'D' #-# ")
        elif(marks <=60 ):
            print("GRADE = 'F' FAIL '_' ")
            break    
        else:
            print("RESULT IS NOT FOUND")   
print(main())
