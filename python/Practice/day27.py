password=input("Enter pass: ")
letters=list(password)
special_chars = [
    "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",",
    "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\",
    "]", "^", "_", "`", "{", "|", "}", "~"
]

up_count=0
low_count=0
dig_count=0
spl_count=0
len_count=0
if len(letters)>=8:
    len_count+=1
for i in letters:
    if i.isupper():
        up_count+=1
    elif i.islower():
        low_count+=1 
    elif i.isdigit():
        dig_count+=1
    elif i in special_chars:
        spl_count+=1
if up_count!=0 and low_count!=0 and dig_count!=0 and spl_count!=0 and len_count!=0:
    print("Strong password")
else:
    print("Weak password")