a = {
    "Javed":100,
    "Jiya":98,
    "Fiza":78,
    "Shradha khapra":60
}

# Return the value of dict in list and tuple

print(a.items())

# Return a key 

print(a.keys())

# Update the value of key

a.update({"Jiya":100,"Fiza":45})
print(a)

# Return the value of specified key


print(a.get("Javed"))
print(a["Javed"])

print(a,type(a))

# Empty Dictinoary

b = {}
print(type(b))


print("This program was developed by Engr. Muhammad Javed.")
