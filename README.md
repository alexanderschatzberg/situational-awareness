# situational-awareness
A tool to aggregate information on specific topics for researchers and professionals.

Information is retrieved from the sources relevant to user's request via API calls or scraping. The information, along with the user's  provided background, is then passed to a Google Gemini model. The Gemini model returns a summary relevant to the user's background that is saved to a markdown file in the `output ` directory.  

## Info Sources (looking to add more, arxiv is just the start)

- arxiv.org for technical research. Thank you to arXiv for use of its open access interoperability.
- perplexity.ai for more general news. They do a fantastic job of summerizing more mainstream info, so no need to reinvent the wheel here. 
  - Their API is still under development, so we're still waiting on them to release a useable version. 

## How to Use 

Setup: 
- Clone the repository onto your machine 
- Get a Gemini API key (https://ai.google.dev/gemini-api/docs/api-key)
- [Optional, Not Implemented Yet] Get a Perplexity API key (https://www.perplexity.ai/settings/api) if you also want Perplexity insights. This is optional, and actually 
- Create a credentials.py file in the src directory  
    - It should have two functions, one named get_gemini_key() and one named get_perplexity_key(). They should return the string of your respective API keys.
    - This file is ignored by git to avoid sharing your private key
- Set up conda env by running the command `conda env create -f env.yml` from the root of the project

Use: 
- Activate your conda enviornment via `conda activate situational_awareness`
- Configure `user_profile.json` to best meet your use case. 
  - For arxive.org: See see https://arxiv.org/category_taxonomy for a complete list of topics. These are for academic papers. 
  - For news api: add whatever keywords you find interesting! If you leave the array blank, the news api won't be included in the search. 
- Run `main.py`, and check the output directory!

Contact me (afs223@cornell.edu) in the event of an error or with suggestions for improving this tool. 

## Configuring user_profile.json 

- user_bg: should be a string of your professional background and interests. This is what the model uses to determine what's useful to your work, so be detailed!
- days_since: How many days back to search. Pretty self explanitory. 
- sources: 
  - arxive: categories should be a list of all th categories that you're interested in searching. A list of available categories can be found here: https://arxiv.org/category_taxonomy
  - [NOT IMPLEMENTED YET] Perplexity: Set to 1 if you'd also like a perplexity summary (requires an API key) or 0 if don't want one

## Next Steps in Development 

- Wait for Perplexity to make citation based AI available. Everything is implemented on our end - their API is still under development. Once they come out with a better API, we'll use that for more general news aggregation. 
- Make a GUI or website (probably Django) for the project in order to make it more accessible. 
