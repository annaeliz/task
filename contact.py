def insertion(contacts):
        i=input("Name: ")
        j=input("Number: ")
        if (i in contacts):
           print("Name is Already Exist")
        else:
            contacts[i]=j

def updation(contacts,i,j):
    if i in contacts:
        contacts.pop(i)
        print("Enter new value of Name/Number of the Contact")
        values=input("value: ")
        if(values.isnumeric()):
            contacts.update({i:values})
            print("Number is Updated")
        else:
            contacts.update({values:j})
            print("Name is updated")

def remove(contacts):
    n=input("Enter the contact to be removed:")
    if n in contacts:
        contacts.pop(n)
    else:
        print("Please Enter vaild contact")
    
def display(contacts):
    print("Contact Book: ")
    print("Name   Number")
    for i,j in contacts.items():
        print(i,"   ",j)
    print("The list of Contact :")
    print(sorted(contacts.items()))

def countcontact(contacts):
    n=0
    for i in contacts.items():
        n=n+1
    print(n)

def search(contacts):
    s=input("Enter the Name to search: ")
    if s in contacts:
        print("Contact is Present")
        print(s, contacts[s])
    else:
        print("Not Found")
      
            
contact={}
c=0
print("Choice 1: Insertion of Conatct Book\nChoice 2: Upadation in Conatct Book\nChoice 3: Removal of Conatct Book\nChoice 4: Display of Conatct Book\nChoice 5: Counts of Conatct Book\nChoice 6: Search in Conatct Book\n")
while(c<7):
    c=int(input("Enter the choice: "))
    if(c==1):
        insertion(contact)
    elif(c==2):
        n=input("Name of contact to be upadted: ")
        m=contact[n]
        updation(contact,n,m)
    elif(c==3):
        remove(contact)
    elif(c==4):
        display(contact)
    elif(c==5):
        countcontact(contact)
    elif(c==6):
        search(contact)
    else:
        print("exit")


