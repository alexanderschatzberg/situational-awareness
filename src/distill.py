import google.generativeai as genai
from credentials import get_gemini_key


def distill(
    user_bg: str, text_body: list[str], model: str = "gemini-1.5-pro-latest"
) -> str:
    """
    A function that distills the heap of information gathered for the user into a single digestible and useful piece of information.
    Accepts the user's background (str) and the list of text bodies(list[str]) and returns a single piece of markdown.
    Markdown is produced by a gemini model (specified by the model parameter)
    """
    gemini_key: str = get_gemini_key()

    return ""
