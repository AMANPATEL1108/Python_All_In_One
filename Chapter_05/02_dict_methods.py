marks={
    "aman":100,
    "subham":56,
    0:"Okay"
}



# print(marks.keys())
# print(marks.values())
# print(marks.items())

marks.update({"aman":99,"ap":100})

print(marks.items())
print(marks.get("aman")) #Return None if not exist
print(marks["aman"])  #Return error if not exist