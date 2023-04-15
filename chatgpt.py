import openai

global history
history = [
    {
        "role": "user",
        "content": "Hello, how are you?"
    }
] # store messages

def get_key():
    key = open("key.txt", "r").read().strip('\n')
    if not key:
        key = input("Please enter your OpenAI API key: ")
        open("key.txt", "w").write(key)
    return key

openai.api_key = get_key()

def completion_gtp3():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )
    return completion.choices[0]["message"]

def completion_gpt4():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    return completion.choices[0]["message"]

def chat():
    while True:
        prompt = input("You: ")
        if prompt == "exit":
            break
        history.append({
            "role": "user",
            "content": prompt
        })
        gpt_3 = completion_gtp3()
        gpt_4 = completion_gpt4()
        print("GPT-3 :", gpt_3["content"])
        print()
        print("GPT-4 :", gpt_4["content"])
        history.append(gpt_3)
        history.append(gpt_4)

if __name__ == "__main__":
    print("Welcome to the GPT-3 and GPT-4 chatbot!")
    chat()
