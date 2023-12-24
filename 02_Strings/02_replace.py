letter = """Dear <|Name|>,
    you are selected!
     Date: <|Date|> """

name = input("Name? ")
date = input("Date? ")

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)

print(letter)