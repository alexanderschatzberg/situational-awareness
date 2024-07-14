# situational-awareness
A tool to aggregate information on specific topics for researchers and professionals 

Information is retrieved from the sources relevant to user's request via API call or scraping, then passed to a language model (Google Gemini). The language model summarizes the information into a digestale format. 

## Info Sources (looking to add more, arxiv is just the start)

- arxiv.org: Thank you to arXiv for use of its open access interoperability.

## How to Use 

Setup: 
- Gemini API key (https://ai.google.dev/gemini-api/docs/api-key)
- credentials.py: make a file called credentials.py in `src` directory
    - It should have a function named get_gemini_key() that returns the string of your Gemini api key 
- Set up and activate conda env from `env.yml`

Use: 
- Configure `main.py` to best meet your use case. 
- Run the main file, and you should be done. 

Contact me (afs223@cornell.edu) in the event of an error or with suggestions for improving this tool. 
