import json
import os
import random
from datetime import datetime
memory_file = "user_input.json"
def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            return json.load(file)
    return {"name": None}
def save_memory(memory):
    with open(memory_file, "w") as file:
        json.dump(memory, file, indent=4)
memory = load_memory()
def calculater(calculation):
    try:
        result = eval(calculation)
        return f"the result is{result}"
    except Exception:
        return "invalid mathematical expression"
def get_time():
    now = datetime.now()
    return now.strftime("current date and time: %d-%m-%Y %H:%M:%S")
def tell_joke():
    jokes = [
        "why did the programmer quit his job? because he didn't get arrays.",
        "why do python programmers prefer dark mode? because light attracts bugs.",
        "why was computer cold? because it forgot to close its windows."
    ]
    return random.choice(jokes)
def get_response(user_input):
    user_input_lower = user_input.lower()
    if "my name is" in user_input_lower:
        name = user_input_lower.split("my name is")[-1].strip().title()
        memory["name"] = name
        save_memory(memory)
        return f"nice to meet you {name}"
    elif "what is my name" in user_input_lower:
        if memory["name"]:
            return f"your name is {memory['name']}"
        else:
            return "i don't know your name"
    elif "hello" in user_input_lower or "hi" in user_input_lower:
        if memory["name"]:
            return f"hello {memory['name']} how i can assist you today?"
        else:
            return "hello what is your name?"
    elif "calculate" in user_input_lower:
        calculation=user_input_lower.replace("calculate", "").strip()
        return calculater(calculation)
    elif "time" in user_input_lower or "date" in user_input_lower:
        return get_time()
    elif "joke" in user_input_lower:
        return tell_joke()
    elif "help" in user_input_lower:
        return "1.calculate: calculate 2 + 6 \n2.date and time: 'time' or 'date'\n3.jokes: 'tell me a joke'\n4.memory: 'my name is<your name>'\ntype exit to end the conversation"
    else:
        return "i am not sure how to help with that type 'help' to see what i can do"
print("multi tool agent:type 'help' to see available commands or 'exit' to quite")
while True:
    user_input = input("siddhi:")
    if user_input.lower() == "exit":
        print("AI: good bye")
        break
    response = get_response(user_input)
    print("AI:", response)