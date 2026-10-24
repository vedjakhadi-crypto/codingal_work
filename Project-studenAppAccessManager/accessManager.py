print("welcome to the Student App Access Manager! ")

mycamera = 1
mystorage = 4
mymicrophone = 9
mylocation = 16
approved_apps = ["location","microphone"]
restricted_apps = ["storage","camera"]

name = input("What is your name? ")
app = input("Which app do you want to access? ")
a = app.lower()
print(a)

if type(name) == str and type(app) is not int:
    print("Your name and your requested app are a string")

if app in approved_apps and app not in restricted_apps:
    print("You are allowed to use this app.")
elif app not in approved_apps:
    print("You are not allowed to use this app")
else:
    print("Not a valid app")

binary_camera = bin(mycamera)
print(binary_camera)
binary_storage = bin(mystorage)
print(binary_storage)
binary_location = bin(mylocation)
print(binary_location)
binary_microphone = bin(mymicrophone)
print(binary_microphone)

student_permission = mymicrophone|mycamera|mystorage
binary_student_permission = bin(student_permission)
print(binary_student_permission)

if binary_student_permission & binary_camera:
    print("Camera permmisions: cleared")
if binary_student_permission & binary_storage:
    print("storage permmisions: cleared")
if binary_student_permission & binary_location:
    print("location permmisions: cleared")
if binary_student_permission & binary_microphone:
    print("microphone permmisions: cleared")

print(binary_camera<<2)
print(binary_storage>>2)

if app == "location" or app == "microphone":
    print("Access granted")
elif app == "storage" or app == "camera":
    print("Access denied")
else:
    print("Not valid")