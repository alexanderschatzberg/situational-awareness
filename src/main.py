from distill import distill
from info_srcs.aggregate import aggregate

# Change these values as desired

# see https://arxiv.org/category_taxonomy for a complete list of topics
topics: list[str] = ["cs.AI", "cs.CE", "cs.ET", "econ.EM", "econ.GN", "stat.ML"] 

user_bg = "I'm a student with a background in computer science. I'm interested in staying up to date with the latest research in artifical intelligence, general economics that could inform my decisions as an investor, and new any new technologies that show promise. I'm also developing a tool that aggregates information from multiple sources and summerizes it for the user using an LLM, so I'm interested in any research that could help me with that. Thank you!"
days_back = 7  # Number of days back to search



def main(topics: list[str], user_bg: str, days_back: int):
    """
    Main function that orchestrates the entire pipeline.
    Takes a list of topics, the user's background, and the number of days back to search
    Aggregates information from the list of sources (right now it's just the arxiv)
    Passes heap of info + user background to gemini model for relevant summerization
    """

    print("Searching sources for relevant information...")
    info: list[dict] = aggregate(topics, days_back)

    print(f"Found {len(info)} papers.")

    print("Distilling information...")

    distill(
        user_bg=user_bg,
        text_body=info,
    )  # Generates md file with distilled info 

if __name__ == "__main__":
    main(topics, user_bg, days_back)
