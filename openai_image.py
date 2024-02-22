import openai
from openai import OpenAI
import requests 
from PIL import Image 
import creds

def generate():
    client = OpenAI(api_key = creds.secret_key)

    print("Dall-E model type: ")
    modeltype = "dall-e-3" if int(input()) == 3 else "dall-e-2"

    print("Text to generate: ")
    text = str(input())

    response = client.images.generate(
        model = modeltype,
        prompt = text,
        size = "1024x1024", 
        quality="hd",
        n=1,
    )

    image_url = response.data[0].url

    return image_url 


if __name__ == "__main__":
    generate()