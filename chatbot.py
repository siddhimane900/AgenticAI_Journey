def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "your name" in user_input:
        return "I am a simple AI chatbot created as part of an Agentic AI learning journey."

    elif "python" in user_input:
        return "Python is a powerful and beginner-friendly programming language widely used in AI and data science."

    elif "agentic ai" in user_input:
        return "Agentic AI refers to AI systems that can autonomously plan and perform tasks to achieve goals."

    elif "goa" in user_input:
        return "Goa is a beautiful destination known for its beaches, forts, and vibrant nightlife."

    elif "help" in user_input:
        return "You can ask me about Python, Agentic AI, or general greetings."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

print("🤖 AI Chatbot: Hello! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("AI: Goodbye! 👋")
        break
    response = get_response(user_input)
    print("AI:", response)