import json
import os
memory_file = "user_memory.json"
def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            return json.load(file)
    return {"name": None, "favorite language": None}
def save_memory(memory):
    with open(memory_file, "w") as file:
        json.dump(memory,file,indent = 4)
memory = load_memory()
def get_response (user_input):
    user_input_lower = user_input.lower()
    if "my name is" in user_input_lower:
        name=user_input_lower.split("my name is")[-1].strip().title()
        memory["name"]= name
        save_memory(memory)
        return f"nice to meet you,{name}"
    elif "what is my name" in user_input_lower:
        if memory["name"]:
            return f"your name is {memory['name']}"
        else:
            return "i don't know your name. please tell me."
    elif "my favorite language is" in user_input_lower:
        language=user_input_lower.split("my favorite language is")[-1].strip().title()
        memory["favorite language"]=language
        save_memory(memory)
        return f"{language} is very good choice"
    elif "what is my favorite language" in user_input_lower:
        if memory["favorite language"]:
            return f"your favorite language is {memory['favorite language']}"
        else:
            return "i don't know your favorite language"
    else:
        return "i am still learning.please try asking something else."
print("memory agent: hello! type 'exit' to end the conversation")

while True:
    user_input =input("Sddhi:")
    if user_input.lower()=="exit":
        print("AI:goodbye")
        break
    response = get_response(user_input)
    print("AI:",response)