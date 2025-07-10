
strin = "Hello World Good Morning"
vowels = "aeiouAEIOU"

vowels_c = 0
constants_c = 0

for i in range(len(strin)):
    if strin[i] in vowels:
        vowels_c = vowels_c + 1
    else:
        constants_c = constants_c + 1

print("vowels_count",vowels_c)
print("consonants_c",constants_c)