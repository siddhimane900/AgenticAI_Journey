import subprocess
def get_llm_response(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt ],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except Exception as e:
        return f"error: {e}"
print("LLM_Based Agent (Mistral)")
print("Type 'exit' to quite.\n")
while True:
    user_input = input("Siddhi:")
    if user_input.lower()== "exit":
        print("AI: Goodbye!")
        break
    response = get_llm_response(user_input)
    print("AI: ",response)