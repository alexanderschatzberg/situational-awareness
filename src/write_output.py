import datetime 

def write_output(gemini_summary: str, text_body) -> None:
    """
    A function that writes the output of the pipeline to a markdown file.
    Accepts the perplexity response, the gemini summary, and the text body.
    """
    file = open(f"output/output-{datetime.date.today().strftime('%Y%m%d%H%M%S')}.md", "w")

    file.write(gemini_summary)

    # file.write("## Perplexity Response: \n" + perplexity_res)

    file.write("\n\n## Source Information: \n")
    for i in text_body:
        file.write((i["title"] + ": " + i["url"] + "\n"))