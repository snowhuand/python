"""
Week 4
- Next week ->Mid term test!!!
- Test : 9am SHARP!!! (1 hour test)
- Format: 12 MCQ (12 marks) + 5 written (12 marks)
- Evaluate expression (precedence of operator)
- Predict the output: Explain how the code starts, where does it branch to....,
finally write the output at the bottom.
- write code: function!!! File IO!!! Except!! Know when diff types of except comes out.
- String: format()
- Lecture 1-4
- How to prepare:
    - Practice!!!
"""
name = str(input("Name:"))
name_lower = name.lower()
#vowels = "aeiouAEIOU"
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for each in name_lower:
    if each in vowels:
        count += 1

print("Out of {} letters, {} has {} vowels".format(len(name), name, count))