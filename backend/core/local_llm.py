import ollama
def askai(prompt):
    response = ollama.chat(model='tinyllama',
                           messages=[
                               {'role':'user',
                                'content':prompt
                                }
                           ]
                           )
    return response['message']['content']