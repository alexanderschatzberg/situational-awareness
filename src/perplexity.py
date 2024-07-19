## Will implement function to search newsapi.ai for relevant articles 
from credentials import get_perplexity_key
import requests


def search_perplexity(user_bg: str) -> str:
    # url = "https://api.perplexity.ai/chat/completions"

    # payload = {
    #     "model": "llama-3-70b-instruct",
    #     "messages": [
    #         {
    #             "role": "system",
    #             "content": "Provide the user with a good picture of current events/news relevant to their background. Cite your sources."
    #         },
    #         {
    #             "role": "user",
    #             "content": f"{user_bg}"
    #         }
    #     ],
    #     "max_tokens": 2000,  # Adjust this value as needed
    #     "temperature": 0.7,  # Add temperature for response variability
    #     "return_citations": True
    # }
    # headers = {
    #     "accept": "application/json",
    #     "content-type": "application/json",
    #     "authorization": f"Bearer {get_perplexity_key()}"
    # }

    # try:
    #     response = requests.post(url, json=payload, headers=headers)
    #     response.raise_for_status()  # This will raise an exception for HTTP errors
    #     return response.json()
    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")
    #     print(f"Response content: {response.text}")
    #     return None
    return "Perplexity has not yet made their API available for public use. Please check back later."