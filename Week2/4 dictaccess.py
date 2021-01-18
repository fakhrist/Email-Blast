thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964   
}
print(thisdict)

x = thisdict["model"]
thisdict["year"] = 2018

print(x)
print(thisdict)

for x in thisdict:
    print(x)