import inflect

print("Spell numbers in English\n")
user_input = int(input("Number: "))
p = inflect.engine()
spell = p.number_to_words(user_input)
print(spell)
