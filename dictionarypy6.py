thisdict={
   "kpopband":{
        "company":"YG",
        "band":"BlackPink",
        "members":4
},
    "kpopband2":{
        "company":"JYP",
        "band":"Twice",
        "members":7
        
    }
}
print(thisdict)
x = thisdict.get("members")
print(x)

thisdict["company"]="JYP"
print(thisdict)

thisdict["year"]=2016
print(thisdict)

x=('key1','key2','key3')
y=22

thislist=dict.fromkeys(x,y)
print(thislist)

print(type(y))