import openai
import os
import csv
import datetime

# top_p computes the cumulative probability distribution,
# and cut off as soon as that distribution exceeds the value of top_p.
# For example, a top_p of 0.3 means that only the tokens comprising the top 30% probability mass are considered.

# Temperature controls randomness, so a low temperature is less random (deterministic),
# while a high temperature is more random.


from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

#No_of_attempts = 10
temperature_step = .5
top_p_step = .5
repeat_count = 2
questions = [("if I have an iphone and a projector, how do I connect them?", "give me a three line response"),
             ("which is the safest vehicle?", "give me a three line response"),
             ("how many leg bones does a whale have?", "give me a three line response")
             ]

openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key="")
COMPLETIONS_MODEL = "gpt-4"


def get_completion(i_question, i_prompt, i_temperature, i_top_p):
    prompt = f"""
    {i_prompt}
    ```{i_question}```
    """

    messages = [{"role": "user", "content": prompt}]

    print("Messages:", messages, "\ttemperature:", i_temperature, "\ttop_p:", i_top_p)
    response = client.chat.completions.create(
        messages=messages,
        temperature=i_temperature,
        top_p=i_top_p,
        model=COMPLETIONS_MODEL
    )
    res = response.choices[0].message.content
    print("Response:", res)
    embedded_value = client.embeddings.create(
        model="text-embedding-ada-002",
        input=[res]
    )
    return res, embedded_value.data[0].embedding


# def randomizer():
#    import random
#    random_number = random.uniform(0, 2)
#    return random_number


# def randomize_p():
#    import random
#    random_number = random.uniform(0, 1)
#    return random_number


def try_values():
    time_stamp = datetime.datetime.now()
#    text = f"""
#    if I have a dvd player and a projector, how do I connect them?
#    """
    file_path = 'dump.csv'
    file_exists = os.path.exists(file_path)

    with open('dump.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['time_stamp', 'sequence', 'repeat', 'temperature', 'top_p', 'question', 'prompt', 'response'])
#        writer.writerow(['Iteration', 'temperature', 'top_p', 'response', 'embedding Value'])

        x = 0
        for repeat in range(0,repeat_count):
            for (text, prompt) in questions:
                temperature = 0
                while temperature <= 1:
                    top_p = 0
                    while top_p <= 1:
                        response, embedding_value = get_completion(text, prompt, temperature, top_p)
                        print("Iteration:", x, "\ttemperature:", temperature, "\ttop_p:", top_p, "\tresponse:", response)
            #            writer.writerow([x, temperature1, top_p1, response, embedding_value])
                        writer.writerow([time_stamp, x, repeat, temperature, top_p, text, prompt, response])

                        top_p = top_p + top_p_step
                        x = x + 1
                    temperature = temperature + temperature_step

    file.close()


try_values()
