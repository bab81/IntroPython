# goal: replace voiwel with g

def translate(phrase):
    translation = ""
    #vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    vowels = ["a", "e", "i", "o", "u"]

    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter

    return  translation

print(translate(input("Enter a phrase: ")))