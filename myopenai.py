from openai import OpenAI
from pydantic import BaseModel

from settings import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


class IDInfo(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    birthday: str
    id_number: str
    address: str
    expired: str


def chat_with_gpt_get_info(image: str, model="gpt-4o-mini") -> str:
    prompts = ("Please read the information in this ID image and return it in JSON format. Note: "
               "Note, please interpret according to the following rules:"
               "Rule 1: Please determine the required content according to the title in the picture, "
               "the title is usually above the content."
               "such as: given name or first name is first name, middle name is the middle name. "
               "Rule 2: Each name may contain multiple spaces. "
               "Rule 3: If there is a single line for the middle name and the first name contains spaces, "
               "do not split the first name, it is a complete first name including spaces."
               "Rule 4: if there is no middle name, set it to empty."
               "Rule 5: A comma or period cannot be part of a name; it is a separator."
               "Rule 6: the format of birthday is 'YYYY-MM-DD'. '"
               "Rule 7: The language of the ID can be English and Filipino. ")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompts
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image
                    }
                }
            ]
        }
    ]

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=messages,
        response_format=IDInfo,
    )

    # print(completion.choices[0].message)
    response = completion.choices[0].message.parsed

    return response.model_dump_json()
    # return response
