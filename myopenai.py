from openai import OpenAI
from pydantic import BaseModel

from settings import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

def chat_with_gpt(messages: [], model="gpt-4o-mini") -> str:
    answer = ""

    # completion = client.chat.completions.create(
    #     model=model,
    #     messages=messages,
    #     response_format=CalendarEvent,
    #     stream=False,
    # )
    completion = client.beta.chat.completions.parse(
        model=model,
        messages=messages,
        response_format=PersonIDEvent,
    )

    # print(completion.choices[0].message)
    response = completion.choices[0].message.parsed

    return response.model_dump_json()


class PersonIDEvent(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    birthday: str
    id_number: str
    address: str
    expired: str
    pass
