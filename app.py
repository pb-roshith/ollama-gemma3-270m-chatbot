import requests

def chat_with_ollama(user_input, history):
    
    model = "gemma3:270m"
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}

    messages = history + [{"role": "user", "content": user_input}]
    payload = {"model": model, "messages": messages, "stream": False}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    reply = data.get("message", {}).get("content", "")
    return reply, messages + [{"role": "assistant", "content": reply}]

def main():

    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        reply, history = chat_with_ollama(user_input, history)
        print(f"AI: {reply}\n")

if __name__ == "__main__":
    main()