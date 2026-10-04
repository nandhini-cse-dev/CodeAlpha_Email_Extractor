import re

with open("input.txt", "r") as file:
    text = file.read()

emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    text
)

print("Found email addresses:")

for email in emails:
    print(email)
    with open("emails.txt", "w") as file:
        for email in emails:
            file.write(email + "\n")
            print("📁 Email addresses saved to emails.txt")