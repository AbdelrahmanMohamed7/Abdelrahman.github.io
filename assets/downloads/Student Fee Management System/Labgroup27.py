def userlogin():
      print("******** STUDENT FEE MANAGEMENT SYSTEM *********")
      userid = input("Please enter your user ID: ")
      userpass = input("Please enter your password: ")
      with open("userpass.txt","r") as fh:
            foundrec = "notfound"
            for recline in fh:
                  reclist = recline.strip().split(":")
                  if reclist[0] == userid and reclist[1] == userpass:
                        foundrec = reclist
                        break
            if foundrec == "notfound":
                  print("Login not successful...!!!")
            else:
                  print("Login Successful...")
      return foundrec

def genid(perm):
      with open("id.txt","r") as idfh:
            rec = idfh.readline()
            reclist = rec.strip().split(":")
      if perm == "staff":
            pref = "STF"
            oldid = reclist[0][3:]
      elif perm == "student":
            pref = "STD"
            oldid = reclist[1][3:]
      nextid = int(oldid) + 1
      if len(str(nextid)) == 1:
          newid = "0000"+str(nextid)
      elif len(str(nextid)) == 2:
          newid = "000"+str(nextid)
      elif len(str(nextid)) == 3:
          newid = "00"+str(nextid)
      elif len(str(nextid)) == 4:
          newid = "0"+str(nextid)
      elif len(str(nextid)) == 5:
          newid = str(nextid)
      newid = pref+newid
      if perm == "staff":
            reclist[0] = newid
      else:
            reclist[1] = newid
      rec = ":".join(reclist)
      with open("id.txt","w") as fh:
            fh.write(rec)
      return newid
            
      
      
     

      
def addstaff():
      userid = genid("staff")
      userpass = userid
      print("User ID :",userid)
      print("User Password:",userpass)
      usrname = input("Please enter you name :")
      acctype = "2"
      with open("userpass.txt","a") as fh:
            rec = userid+":"+userpass+":"+usrname+":"+acctype+"\n"
            fh.write(rec)
      
def addstudent():
      userid = genid("student")
      userpass = userid
      print("Student ID :",userid)
      print("Student Password:",userpass)
      usrname = input("Please enter you name :")
      acctype = "3"
      with open("userpass.txt","a") as fh:
            rec = userid+":"+userpass+":"+usrname+":"+acctype+"\n"
            fh.write(rec)   
def dispalluser():
      with open("userpass.txt","r") as fh:
            for rec in fh:
                  reclist = rec.strip().split(":")
                  
      
def superusermenu():
      while True:
            print("SUPER USER MENU")
            print("===============")
            print("\n\t1. Add new admin staff account")
            print("\t2. Display All user accounts")
            print("\t3. LOGOUT from the system")
            ans = input("Please enter your choice :")
            if ans == "1":
                  addstaff()
            elif ans == "2":
                  dispalluser()
            elif ans == "3":
                  break
            
      

def adminstaffmenu():
        while True:
            print("ADMIN STAFF MENU")
            print("===============")
            print("\n\t1. Add new Student account")
            print("\t2. Display All user accounts")
            print("\t3. LOGOUT from the system")
            ans = input("Please enter your choice :")
            if ans == "1":
                  addstudent()
            elif ans == "2":
                  dispalluser()
            elif ans == "3":
                  break
            

def studentmenu():
      pass






#MAIN LOGIC
#==========
while True:
      loginstat = userlogin()
      if loginstat != "notfound":
            print("Welcome to the System "+loginstat[2])
            if loginstat[3] == "1":
                  superusermenu()
            elif loginstat == "2":
                  adminstaffmenu()
            elif loginstat == "3":
                  studentmenu()
      else:
            print("INVALID LOGIN CREDENTIALS...!!!!")
      ans = input("Press Q to Quit the SYSTEM.. Anyother Key to Continu....")
      if ans == "Q":
            break
      
