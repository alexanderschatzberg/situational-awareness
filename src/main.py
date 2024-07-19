from distill import distill
from perplexity import search_perplexity
from write_output import write_output
from info_srcs.aggregate import aggregate
import json

def main(user_profile: str = "user_profile.json"):
    """
    Main function that orchestrates the entire pipeline.
    Takes a list of topics, the user's background, and the number of days back to search (all provided in user_profile.json)
    Aggregates information from the list of sources
    Passes heap of info + user background to gemini model for relevant summerization
    """
    user_profile = json.load(open(user_profile))
    user_bg =  user_profile["user_bg"]
    days_back = user_profile["days_back"]
    sources = user_profile["sources"]

    print("Searching sources for relevant information...")
    info: list[dict] = aggregate(sources=sources, days_back=days_back, user_bg=user_bg)

    print(f"Found {len(info)} papers.")

    print("Distilling information...")

    gemini_summary = distill(
        user_bg=user_bg,
        text_body=info,
    )  # Generates md file with distilled info 

    print("Searching for relevant news articles...")

    perplexity_res = search_perplexity(user_bg)

    write_output(perplexity_res, gemini_summary, info)

    print("Output has been written!.")

if __name__ == "__main__":
    main()
