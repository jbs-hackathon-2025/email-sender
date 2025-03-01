from  openai import OpenAI

email = "2025.kzheng@jburroughs.org"
client = OpenAI()

def hackedEmailPrompt(email, recipient):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "developer",
            "content": """You are writing an email to inform
            somebody that they were sent an email from a suspicious sender. 
            """
        },
        {
            "role": "user",
            "content": f"""
            write the body of an email that tells the user that they have received 
            a suspicious email from {email}, address the email to {recipient}, and have it be sent from the sAIf team. Leave the subject line out of the response.
            """
        }
        ]
    )
    #print(completion.choices[0].message)
    return completion.choices[0].message.content

