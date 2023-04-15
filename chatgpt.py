import openai
from termcolor import colored

global history
history = [
    {"role": "system", "content": "Only respond with a joke, Okay"},
    {"role": "system", "content": "Okay"},
]

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
        print()
        if prompt == "exit":
            break
        history.append({
            "role": "user",
            "content": prompt
        })
        gpt_3 = completion_gtp3()
        
        gpt_4 = completion_gpt4()
        print()
        print(colored(f"GPT-3: {str(gpt_3.content)}", "green"))
        print(colored(f"GPT-4: {str(gpt_4.content)}", "blue"))
        history.append(gpt_4)

if __name__ == "__main__":
    print("Welcome to the GPT-3 and GPT-4 chatbot!")
    chat()
