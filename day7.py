def calculator(calculation):
    try:
        result= eval(calculation)
        return f"The result is {result}"
    except:
        return "Invalid mathematical expression.please try again."
def getresponse(user_input):
    user_input_lower=user_input.lower()
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hello ! I am your tool_usingagent\n You can ask me to perform calculations.\n" \
        " Example:calculate  2 + 3\n Type 'help' for more information or 'exit' to quite"
    elif "help" in user_input_lower:
        return "help-how to use this calculator agent\n 1.to perform a calculation,type:calculate <calculation> \n" \
        "2.supported oprations:+,-,*,/\n 3. Type 'exit' to end the conversation."
    elif "calculate" in user_input_lower:
        calculation=user_input_lower.replace("calculate","").strip()
        if calculation == "":
            return "provide a mathemathetical expression.Example: calculate 4 + 3"
        return calculator(calculation)
    else:
        return "I am not sure how to help with that \n try typing 'calculate 2 + 4' or type 'help' for guidence."
print("tool using agent:hello type 'hello' to begin or 'exit' to quite")
while True:
    user_input=input("Siddhi:")
    if user_input.lower()=="exit":
        print("AI:Goodbye.Have a great day")
        break
    response=getresponse(user_input)
    print("AI:",response)