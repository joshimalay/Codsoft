def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"
    elif 'how are you' in user_input:
        return "I'm just a program, but I'm doing well! How about you?"
    elif 'what is your name' in user_input or 'who are you' in user_input:
        return "I'm a simple chatbot created to help you with basic questions."
    elif 'what is python' in user_input:
        return "Python is a high-level, interpreted programming language known for its simplicity and readability."
    elif 'what can you do' in user_input:
        return "I can answer simple questions based on predefined rules!"
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a great day!"
    elif 'what is ai' in user_input:
        return "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines."
    elif 'what is machine learning' in user_input:
        return "Machine Learning is a subset of AI that involves training algorithms to make predictions or decisions based on data."
    elif 'what is your favorite color' in user_input:
        return "I don't have preferences, but I think the color blue is calming!"
    elif 'what is the capital of france' in user_input:
        return "The capital of France is Paris."
    elif 'tell me a joke' in user_input:
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif 'who is the president of the usa' in user_input:
        return "As of my last update, the President of the USA is Joe Biden."
    elif 'what is the largest planet' in user_input:
        return "The largest planet in our solar system is Jupiter."
    elif 'what is the speed of light' in user_input:
        return "The speed of light is approximately 299,792 kilometers per second."
    elif 'how many continents are there' in user_input:
        return "There are seven continents on Earth: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."
    elif 'what is 2+2' in user_input:
        return "2 + 2 equals 4."
    elif 'do you like humans' in user_input:
        return "I don't have emotions, but I think humans are interesting and creative beings!"
    elif 'can you learn' in user_input:
        return "I'm a simple chatbot, so I can't learn, but more advanced AI systems can learn from data."
    elif 'what is the meaning of life' in user_input:
        return "That's a deep question! Some say it's 42, others find meaning in love, happiness, and purpose."
    elif 'how old are you' in user_input:
        return "I was created recently, so I'm quite young in human terms!"
    elif 'what is your purpose' in user_input:
        return "My purpose is to assist you with simple queries and help you understand basic concepts."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

print("Chatbot: Hi there! You can start typing to chat with me.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot: " + chatbot_response(user_input))
        break
    else:
        print("Chatbot: " + chatbot_response(user_input))
