import requests

ollama_url = "http://localhost:11434/api/chat"

def get_ai_response(prompt):
    payload = {
        "model": "qwen3.5:4b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
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
    while True:
        print("\n===== AI TEXT ASSISTANT =====")
        print("1. Summarize Text")
        print("2. Explain the concept in simple words.")
        print("3. Answer the user's question.")
        print("4. Exit")
        
        option = input("Choose an option(1-4): ").strip()

        if option == '4' or option.lower() == 'exit':
            print("Goodbye!")
            break

        if option == '1':
            user_input = input("Enter the text you want to summarize: ")
            if not user_input.strip():
                print("Please enter some text.")
                continue
            prompt = f"Summarize the following text clearly and concisely:\n{user_input}"
            
        elif option == '2':
            user_input = input("Enter the concept you want explained: ")
            if not user_input.strip():
                print("Please enter some text.")
                continue
            prompt = f"Explain the following concept in simple words. Include one easy example:\n{user_input}"
            
        elif option == '3':
            user_input = input("Ask your question: ")
            if not user_input.strip():
                print("Please enter some text.")
                continue
            prompt = user_input
            
        else:
            print("Please give a valid input (1, 2, 3, or 4).")
            continue

        # Get response from the API function
        answer = get_ai_response(prompt)

        # Print layout handled here in main
        if answer:
            print("\nAI:", answer)
            print("-" * 20)
        else:
            print("AI could not generate a response. Please try again.")

if __name__ == "__main__":
    main()
