import google.generativeai as genai
from credentials import get_gemini_key
import datetime


def distill(
    user_bg: str, text_body: list[str], model_name: str = "models/gemini-1.5-pro-latest"
) -> None:
    """
    A function that distills the heap of information gathered for the user into a single digestible and useful piece of information.
    Accepts the user's background (str) and the list of text bodies(list[str]) and returns a single piece of markdown.
    Markdown is produced by a gemini model (specified by the model parameter)
    """
    
    gemini_key: str = get_gemini_key()
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel(model_name, safety_settings={
        
    })

    general_instruction = "General Instruction: You are an AI model designed to summarize recently published information. Your summary should be tailored to the user's background."

    print(f"Tokens in gathered content: {model.count_tokens(str(text_body))}")


    response = model.generate_content(
        general_instruction
        + "\nUser Background: "
        + user_bg
        + "\nContent to be Summarized: "
        + str(text_body)
    )

    return response.text