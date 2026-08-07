from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items  = list(path.rglob('*'))
    print("Existing file are :")
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:

        readfileandfolder()
        name = input("Enter the name of this file :- ")
        p=Path(name)
        if not p.exists() and p.is_file():

            with open(p,'w') as file:
                data = input("What do want to write :")
                file.write(data)

            print("File create successfully ")

        else :
            print("File is alredy exist ")

    except Exception as err:
        print(err)


def readfile():
    
    try:

        readfileandfolder()
        name  = input("Which file you want to read :")
        p=Path(name)

        if p.exists() and p.is_file():
            with open(p,'r') as file:
                data = file.read()
                print(data)
            print("Read it successfully")

        else :
            print("This file does not exist")

    except Exception as ex:
        print(ex)
        
        
def  update_file():
    
    try:
    
        readfileandfolder()
        name = input("Which file you want to updte :")
        p=Path(name)
        if p.exists() and p.is_file():
            
            print("Press 1 for updating name ")
            print("Press 2 for overwrite the data ")
            print("Press 3 for append the data ")
            
            pres =int(input("Enter the option :"))
            
            if pres == 1:
                name2 = input("Tell your new file name :")
                p2=Path(name2)
                p.rename(p2)
                print(f"File {p2} update successfully")
                
            if pres== 2:
                with open(p,'w') as file:
                    data = input("What do want to write but your data is over written  :")
                    file.write(data)
                print("Data overwrite successfully")
                    
            if pres == 3:
                with open (p,'a') as file:
                    data = input("What do want to append :")
                    file.write(" "+data)
                print("Data append Succeccfully")
        else:
            print("This file dose not existed")
                
    except Exception as ex:
        print(ex)  
        
def delete_file():
    try:
        readfileandfolder()
        name = input("Which file you want to delete :")
        p=Path(name)
        
        if p.exists() and p.is_file():
            os.remove(p)
            print("File remove successfully")
            
        else:
            print("File does not Exist")
    except Exception as ex:
        print(ex)
        
        
                
print("press 1 for creat a file")
print("press 2 for read  file")
print("press 3 for update  file")
print("press 4  for delete  file")


check=int(input("Please tell your response :"))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check==3:
    update_file()
    
if check ==4:
    delete_file()