import urllib, urllib.request
from distill import distill
from info_srcs.aggregate import aggregate


def main():
    """
    Main function that orchestrates the entire pipeline.
    Takes a list of topics, the user's background, and the number of days back to search
    Aggregates information from the list of sources (right now it's just the arxive)
    Passes heap of info + user background to gemini model for relevant summerization
    """

    # Change these values as desired
    topics: list[str] = [
        "cs.AI",
        "econ.GN",
    ]  # see https://arxiv.org/category_taxonomy for a complete list of topics

    user_bg = "I'm a machine learning engineer looking to stay up-to-date with the latest research in AI in order to stay competitive in the field. My work is primarily focused on the overlap between artifical intelligence and robotics, but I'm interested in hearing about research across the field. I also am interested in economic research that may be relevant to my life as an investor."
    days_back = 4  # Number of days back to search

    info = aggregate(topics, days_back)
    print(info)

    # final_output = distill(
    #     user_bg=user_bg,
    #     text_body=info,
    # )

    # print(final_output)


if __name__ == "__main__":
    main()
