print("Welcome to the character occurance program")

text = input("Enter some text.")
character = input("Enter the thing that needs to be searched ")

i=0
counter=0

while (i<len(text)):
    if (text[i]==character):
        counter+=1
    i=i+1
print("The charcter", character, "you were looking for in the text" ,text ,"has occured",counter ,"times")