import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")


def generate_gpt3_response(user_text, print_output=False):
    completions = openai.Completion.create(
    model="text-davinci-003",  # Determines the quality, speed, and cost.
    prompt=user_text,           # What the user typed in
    temperature=0.7,            # Level of creativity in the response
    max_tokens=256,             # Maximum tokens in the prompt AND response
    top_p=1,                    # The number of completions to generate
    frequency_penalty=0,
    presence_penalty=0,
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

print("\n\n\n\n\nPrompt ChatGPT\n")


question = input("Faça uma pergunta:\n")

while question != "":
    print(generate_gpt3_response(question))
    print("\n\n####################################################\n\n")
    print('Pressione "Enter" para sair, ou...')
    question = input("Faça uma pergunta pergunta:\n")

print("Saindo.")