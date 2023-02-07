import re


# method - 1

def RemoveWords(toPrint):
    pattern = re.compile("\\b(b1/|b2/|b3/|b4/|copy)\\W", re.I)
    return pattern.sub("", toPrint)
    
toPrint = "/data/AUH SME & HOUSING Docs From 1st-APR-2022 /b1/(copy)/20-APR-2022/PDD/LNADB02621-220225024.pdf"
    
print(RemoveWords(toPrint))

# method - 2

file = "/data/AUH SME & HOUSING Docs From 1st-APR-2022 /b1/b3/11-APR-2022/DOCKET/DOCKET.xlsx"
words_remove = ["/b1/","/b2/", "/b3/","/b4/", "(copy) /", " (copy)/"]

for word in words_remove :
    if word in file:
        string = file.replace(word, '/')
        print(string)

# method - 3 

def remove_words(text, words_to_remove):
    words = text.split() 
    filtered_words = [word for word in words if word not in words_to_remove]
    return " ".join(filtered_words) 
text = "/data/AUH SME & HOUSING Docs From 1st-APR-2022 /b3/20-APR-2022/PDD/LNADB02621-220225024.pdf"
words_to_remove = ["/b1", "/b2", "/b3", "/(copy)"]
print(remove_words(text, words_to_remove))

# method - 4

def remove_words(input_string, words_to_remove):
    regex = r"\b(" + "|".join(words_to_remove) + r")\b"
    return re.sub(regex, "", input_string)

input_string = "/data/AUH SME & HOUSING Docs From 1st-APR-2022 /b3/20-APR-2022/PDD/LNADB02621-220225024.pdf"
words_to_remove = ["/b1", "/b2", "/b3"]
output_string = remove_words(input_string, words_to_remove)

print(output_string)