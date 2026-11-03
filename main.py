import requests

ollama_url = "http://localhost:11434/api/chat"

def get_ai_response(history):
    payload = {
        "model": "qwen3.5:4b",
        "messages": history,
        "stream": False,
        "think": False,
        "keep_alive": "10m",
        "options": {
            "num_predict": 300
        }
    }
    try:
        response = requests.post(
            ollama_url,
            json=payload,
            timeout=180
        )
        
        response.raise_for_status()
        data = response.json()
        
        return data.get("message", {}).get("content", "")
            
    except requests.exceptions.Timeout:
        print("Ollama response timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("Cannot connect to Ollama. Check whether it is running.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None


    


def main():

    chat_history = []

    print("\n=================================")
    print("       AI TEXT ASSISTANT")
    print("=================================")
    print("Chatbot initialized! Ask me anything.")
    print("Type 'exit' to quit.")
    print("Type 'clear' to clear conversation history.")

    while True:

        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Please enter a question.")
            continue

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.lower() == "clear":
            chat_history.clear()
            print("Conversation history cleared!")
            continue

        chat_history.append({
            "role": "user",
            "content": user_input
        })

        answer = get_ai_response(chat_history)

        if answer:
            chat_history.append({
                "role": "assistant",
                "content": answer
            })

            print("\nAI:", answer)

        else:
            chat_history.pop()
            print("AI could not generate a response. Please try again.")


if __name__ == "__main__":
    main()
