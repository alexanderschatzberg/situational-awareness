import requests
import datetime

import xml.etree.ElementTree as ET


def search_arxiv(topic: str, days_back: int) -> list[str]:
    """
    A function that searches arXiv for papers on the given topic pushed in the last `days_back` days.

    """
    print(f"Searching arXiv for papers on {topic} pushed in the last {days_back} days.")

    base_url = "http://export.arxiv.org/api/query?"

    today = datetime.datetime.now(datetime.UTC)
    x_days_ago = today - datetime.timedelta(days=days_back)

    # Format final search query
    search_query = f'cat:{topic} AND submittedDate:[{x_days_ago.strftime("%Y%m%d")}0000 TO {today.strftime("%Y%m%d")}2359]'

    # Define the parameters for the API request
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": 1000,  # Set the maximum number of results to retrieve
    }

    response = requests.get(base_url, params=params)

    # Parse the response if successful
    paper_details = []
    if response.status_code == 200:
        paper_details = parse_arxiv_response(response.text)
    else:
        print(f"Error fetching from the arxiv: {response.status_code}")

    return paper_details


def parse_arxiv_response(response: str) -> list[dict[str, str]]:
    # Parse the XML data into an ElementTree object
    root = ET.fromstring(response)

    # Namespace for arXiv API
    ns = {"arxiv": "http://www.w3.org/2005/Atom"}

    # Extract entries (papers) from the response
    entries = root.findall("arxiv:entry", ns)

    # List to store paper details
    papers = []

    for entry in entries:
        title = entry.find("arxiv:title", ns).text
        authors = [
            author.find("arxiv:name", ns).text
            for author in entry.findall("arxiv:author", ns)
        ]
        url = entry.find("arxiv:link", ns).attrib["href"]

        abstract = entry.find("arxiv:summary", ns).text
        published_date = entry.find("arxiv:published", ns).text

        # Add paper details to the list
        papers.append(
            {
                "title": title,
                "abstract": abstract.strip().replace(
                    "\n", " "
                ),  # Remove leading/trailing whitespace and newlines
                "published_date": published_date,
                "url": url,
            }
        )

    return papers
