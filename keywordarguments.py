#keyword arguments = an argument preceded by an identifier
#                       helps with readibility
#                       order of arguments dosen't matter
#                       1.positional 2.default 3.KEYWORD 4.arbitrary

def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

hello("Hello", "Mr", "Sponge Bob","Square Pants")
hello (first_name="Felipe",title="Mr",last_name="Laurentino",greeting="Hello")