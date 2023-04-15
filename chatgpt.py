import openai

global message_history
global token_count
token_count = 0
message_history = [
    {"role": "system", "content": "You only reply in jokes. Ok?"},
    {"role": "system", "content": "I'm a chatbot that only replies in jokes and I am very good at it."},
]

def get_key():
    key = open("key.txt", "r").read().strip('\n')
    if not key:
        key = input("Please enter your OpenAI API key: ")
        open("key.txt", "w").write(key)
    return key

openai.api_key = get_key()

def completion_gpt_3():
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history
    )
    return completion["choices"][0]["message"]


def completion_gpt_4():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message_history
    )
    return completion["choices"][0]["message"]

def chat(): 
    while True:
        prompt = input("You: ")
        if prompt == "quit":
            break
        message_history.append({"role": "user", "content": prompt})
        res = completion_gpt_3()
        res_gpt_4 = completion_gpt_4()
        print("gpt-3.5-turbo: ", res["content"])
        print("gpt-4: ", res_gpt_4["content"])
        message_history.append(res)

if __name__ == "__main__":
    print("Welcome to the chatgpt CLI jokes ! \nType 'quit' to exit.")
    chat()