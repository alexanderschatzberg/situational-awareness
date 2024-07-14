import urllib, urllib.request
from distill import distill
from info_srcs.aggregate import aggregate


def main():
    """
    Main function that orchestrates the entire pipeline.
    Takes a list of topics, the user's background, and the number of days back to search
    Aggregates information from the list of sources (right now it's just the arxiv)
    Passes heap of info + user background to gemini model for relevant summerization
    """

    # Change these values as desired
    topics: list[str] = [
        "astro-ph.EP",
        "astro-ph.HE",
        "astro-ph.CO",
        "astro-ph.GA",
        "astro-ph.IM",
        "astro-ph.SR",
    ]  # see https://arxiv.org/category_taxonomy for a complete list of topics

    user_bg = "I'm an astronomer who studies supernovae and kilonovae. My observatory is particularly interested in 1A SNe, any research related to kilonovae, and general instrumental methods that could be applied to our facility."
    days_back = 4  # Number of days back to search

    print("Searching sources for relevant information...")
    info = aggregate(topics, days_back)

    print(f"Found {len(info)} papers.")

    print("Distilling information...")

    distill(
        user_bg=user_bg,
        text_body=info,
    )  # Print out is implemented in distill.py

    ## Print out the titles and links to the info that was distilled
    for i in info:
        print(i["title"] + ": " + i["url"])


if __name__ == "__main__":
    main()
