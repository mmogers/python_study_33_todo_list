import random

toDoList = []
color = ["RED", "GREEN", "PURPLE", "CYAN", "BROWN", "BLUE", "LIGHT_GRAY", "YELLOW", "LIGHT_GREEN", "LIGHT_BLUE"]

def myPrint(color, text): 
  if color.upper() == "RED":
    print("\033[0;31m",text,sep="", end="")
  elif color.upper() == "GREEN": 
    print("\033[0;32m",text,sep="", end="")
  elif color.upper() == "PURPLE":
    print("\033[0;35m",text,sep="", end="")
  elif color.upper() == "CYAN":
    print("\033[0;36m",text,sep="", end="")
  elif color.upper() == "BROWN":
    print("\033[0;33m",text,sep="", end="")
  elif color.upper() == "BLUE":
    print("\033[0;34m",text,sep="", end="")
  elif color.upper() == "LIGHT_GRAY":
    print("\033[0;37m",text,sep="", end="")
  elif color.upper() == "YELLOW":
    print("\033[1;33m",text,sep="", end="")
  elif color.upper() == "LIGHT_GREEN":
    print("\033[1;32m",text,sep="", end="")
  elif color.upper() == "LIGHT_BLUE":
    print("\033[1;34m",text,sep="", end="")
  else:
    print("\033[0m",text,sep="", end="")
  print("\033[0m",sep="", end="")

myPrint ("green","TO DO LIST MANAGER\n")

def viewList(list):
  print()
  i = 1
  for item in list:
    number = random.randint(0,9)
    myPrint(color[number],i )
    print(" ", end = "")
    myPrint(color[number],item)
    print()
    i += 1
  print()
  
def add(list):
  item = input ("What do you want to add: ")
  list.append(item)

def edit(list):
  item = input("What do you want to delete: ")
  if item in list:
    list.remove(item)
  else:
    print(f"There is no such thing as - {item} - in the list")


while True:
  toDo = input("\nDo you want to view, add, or edit your to do list? ").lower()
  if toDo == "view":
    viewList(toDoList)
  elif toDo == "add":
    add(toDoList)
  elif toDo == "edit":
    edit(toDoList)
  else:
    print("No such command")



