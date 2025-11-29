import openai

openai.api_key = "کلید-api-شما-اینجا-قرار-میگیرد"

def get_bot_response(user_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما دستیار مودب رستوران زعفرون هستید. منوی ما شامل کباب و جوجه است."},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message['content']
