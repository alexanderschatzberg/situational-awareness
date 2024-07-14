from .arxiv import search_arxiv


def aggregate(topics: list[str], days_back: int) -> list[str]:
    """
    A function that aggregates information on provided topics from the sources in `info_srcs` to be passed to the distillment pipeline.
    Information is gathered from the sources via webscrapping or API calls.
    topics: a list of the topics that you want to search. The list from the arxiv can be found here: https://arxiv.org/category_taxonomy
    days_back: the number of days back to search for papers
    """
    print("Aggregating information on the following topics:", topics)

    info = []
    for topic in topics:
        info.extend(search_arxiv(topic, days_back))

    return info
