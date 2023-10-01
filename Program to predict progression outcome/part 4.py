#AUTHOR: Yasara Gayanaka Dissanayake
##COURSEWORK

count = 0
count1=0
count2=0
count3=0
count4=0
Outcome=''
select='y'
stu_num_list = list()

#List---------
Student_list=[]
#Credit_list=[]#
def choose():
    global count
    print("\nWho are you?\n1.student\n2.staff member")
    x = input()
    if x == "1":
        count = 1
    elif x == "2":
        count = 3
    else:
        print("enter 1 or 2\n ")
        choose()

#Functions-----
def int_input(message,error_message1='Out of range',error_message2='Invalid input integer required'):
       while True:
           try:
                marks= int(input(message))
                if marks not in range(0, 121, 20):
                    print(error_message1)
                    continue
           except ValueError:
               print(error_message2)
               continue
               #break#############
           break
       return marks

def stu_id():
    try:
        print("Enter student ID: W", end="")
        stu_num = int(input())
        if len(str(stu_num)) == 7:
            stu_num_list.append (stu_num)
        else:
            print("ID contains 7 numbers")
            stu_id()
    except:
        print("Input ID correctly without W")
        stu_id()
        
while count != 2:
       choose()
       while True:
           while select=='y':
               stu_id()
               passs=int_input('Enter your passs credit:')
               defer=int_input('Enter your defer credit:')
               fail=int_input('Enter your fail credit:')
               Credit_list=[passs,defer,fail]

           
               total=passs+defer+fail
               total==120
               
                     
               if  passs ==120 and defer==0 and fail==0:
                   Outcome='progress'
                   count1=count1+1
                   
               elif passs==100 and defer<=20 and fail<=20:
                   Outcome='progress(module trailer)'
                   count2=count2+1
                   
               elif  0<=passs<=80 and 20<=defer<=120 and 0<=fail<=60:
                   Outcome='Do not progress-module retriever'
                   count3=count3+1
                   
               elif 0<=passs<=40 and 0<=defer<=40 and 80<=fail<=120:
                   Outcome='Exclude'  
                   count4=count4+1
                   
               else:
                   Outcome='Total incorrect'
               print(Outcome)
               
               Credit_list.append(Outcome)
               Student_list.append(Credit_list)
               if count == 1:
                      quit()
               else:
                      count +=1
                   
               select=str(input("Would you like to enter another data set? \nEnter'y'for yes or 'q' for quit:"))
               print('\n')
               if select =='q':
                   print('------------------------------------------------------------\nHISTOGRAM')
                   print("Progress",count1," :",count1*"*")
                   print("Trailer",count2,"  :",count2*"*")
                   print("Retriever",count3,":",count3*"*")
                   print("Excluded",count4," :",count4*"*")
                   
                   outcomes = count1 + count2 + count3 + count4
                   
                   print("\n",outcomes,"outcomes in total.")
                   print("\n--------------------------------------------------------------------")


                   detailFile=open('Student_list.txt','w')


                   
                   for i in Student_list:
                       x=str(i[0:3])#replace fun. not work on integers#
                       x=x.replace('[','') 
                       x=x.replace(']','')
                       print(i[-1],'-',x)
                       list1 = ((i[-1]+'-'+x))
                       print(list1)
                       detailFile.write(i[-1])
                       detailFile.write('-')
                       detailFile.write(x)
                       detailFile.write('\n')
                   detailFile.close()

                   print("Part 4: ")
                   my_dict ={}
                   q =0
                   while q < outcomes:
                          my_dict["w"+str(stu_num_list[q])] = list1
                          q +=1
                   print(my_dict)
                   #print(Student_list)#####
                   break
               else: 
                   while select != "y" and select != "q":
                       print("Enter an valid input")
                       select=str(input("Would you like to enter another data set? \nEnter'y'for yes or 'q' for quit:"))
                   continue
               break
