import re
## this is chnage 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


if x:
    print ("Match")
else:
    print("NOT MATCH")
