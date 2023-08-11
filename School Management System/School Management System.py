import mysql.connector as a

db = a.connect(host="localhost",user="root",password="",database="School Management System")
command_handler = db.cursor(buffered=True)

while 1:

        print("")
        print("Welcome To The  School Management System")
        print("")
        print("1. Student Login") 
        print("2. Faculty Login")
        print("3. Admin Login")
        
        stud={}
        tchr={}
        
        user_opt=input(str("Login as: "))
        if user_opt == "1":
            print("Logined as Student ")
            print("")
            username = input(str("Username: "))
            password= input(str("Password: "))
            
            if username == "student":

                if password =="password":
                     print("")
                     print("Login Sucessfully") 
                     
                     if len(stud)==0:
                        print("Studetns are still not registered ")
                        break
                     else:
                        print(stud)  
                        break  
                     
                      
                   
            
        elif user_opt == "2":
            print("Logined as Teacher") 
            username = input(str("Username: "))
            password= input(str("Password: "))
            
            if username == "teacher":
                if password =="password":
                     print("")
                     print("Login Sucessfully") 
                     while 1:
                        print("")
                        print("Teacher's Menu")
                        print("1. Register new Student")
                        print("2. view Teacher's list")
                        print("3. logout")
                        
                        user_opt= input(str("Option : "))
                        if user_opt =="1":
                            print("")
                            print("New Student Detail: ")
                            studentname=input(str("Userame: "))
                            studntpassword=input(str("password: "))
                            
                            #command_handler.execute(username,password,"student")
                            #db.commit()
                            
                            print(username+" has been registered as student")
                            stud.add(studentname)
                         
                            break
                        if user_opt =="2":
                            print("")
                            if len(tchr)==0:
                             print("teachers are still not registered ")
                             break
                            else:
                             print(tchr)  
                             break
              
        elif user_opt == "3":
            print("")
            print("Logined as Admin")
            
            print("")
            username = input(str("Username: "))
            password= input(str("Password: "))
            
            if username == "admin":
                if password =="password":
                     print("")
                     print("Login Sucessfully") 
                      
                     while 1:
                        print("")
                        print("Admin Menu")
                        print("1. Register new Student")
                        print("2. Register new Teacher")
                        print("3. logout")
                        
                        user_opt= input(str("Option : "))
                        if user_opt =="1":
                            print("")
                            print("New Student Detail: ")
                            studentname=input(str("Userame: "))
                            studntpassword=input(str("password: "))
                            
                            #command_handler.execute(username,password,"student")
                            #db.commit()
                            stud.update(studentname)
                            
                            print(studentname+" has been registered as student")
                            break
                        
                        if user_opt =="2":
                            print("")
                            print("New Teacher Detail: ")
                            teachername=input(str("Userame: "))
                            password=input(str("password: "))
                            
                            #command_handler.execute(username,password,"student")
                            #db.commit()
                            tchr.update(teachername)
                            print(username+" has been registered as Teacher")
                            break
                        
                        if user_opt =="3":
                            break
                        
                else: 
                   print("")    
                   print("Incorrect Password")
                   break
                   
            else:
                 print("")
                 print("Login id mismatched")  
                 break           
                    
        else:
            print("Invalid Login Detail")   
            break 
        
