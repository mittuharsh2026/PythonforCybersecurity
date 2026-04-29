def send_message():
    for i in range(5):
        print("Yeah it is")

# ask user something
answer = input("Is Python easy? ")

# check answer and call function
if answer.lower() == "yes":
    send_message()
else:
    print("No worries, keep practicing")
