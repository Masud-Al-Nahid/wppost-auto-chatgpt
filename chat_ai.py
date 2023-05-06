def chat_gptai(content):
    import openai
    openai.api_key = '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' # supply your API key however you choose
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}
                
                ]
                )
    output_response=completion.choices[0].message.content
    return output_response
