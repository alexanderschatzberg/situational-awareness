from .arxiv import search_arxiv

def aggregate(sources: list[dict], days_back: int, user_bg: str) -> list[str]:
    """
    A function that aggregates information on provided topics from the arxiv and Perplexity to be passed to the distillment pipeline.
    Args are passed from user_profile.py
    """
    print("Aggregating information from the following sources: ", str(sources.keys()))

    info = []

    # Search arxiv 
    arxiv_categories = sources["arxiv"]["categories"]
    for category in arxiv_categories:
        info.extend(search_arxiv(category, days_back))

    return info
