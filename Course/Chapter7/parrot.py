prompt = input("Tell me something,and I will repeat it back to you：")
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
actinve = True
while actinve:
    message = input(prompt)

    if message =='quit':
        actinve = False
    else:
        print(message)