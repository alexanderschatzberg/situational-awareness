# situational-awareness
A tool to aggregate information on specific topics for researchers and professionals.

Information is retrieved from the sources relevant to user's request via API calls or scraping. The information, along with the user's  provided background, is then passed to a Google Gemini model. The Gemini model returns a summary relevant to the user's background. 

## Info Sources (looking to add more, arxiv is just the start)

- arxiv.org: Thank you to arXiv for use of its open access interoperability.

## How to Use 

Setup: 
- Clone the repository onto your machine 
- Get a Gemini API key (https://ai.google.dev/gemini-api/docs/api-key)
- Create a credentials.py file in the src directory  
    - It should have a function named get_gemini_key() that returns the string of your Gemini api key 
    - This file is ignored by git to avoid sharing your private key
- Set up conda env by running the command `conda env create -f env.yml` from the root of the project

Use: 
- Activate your conda enviornment via `conda activate situational_awareness`
- Configure `main.py` to best meet your use case. 
- Run the main file, and you should be done. 

Contact me (afs223@cornell.edu) in the event of an error or with suggestions for improving this tool. 


## Next Steps in Development 

- Continue to add more sources. These will likely include social platforms, other databases of published research, and niche sources of info. 
- Implement a smart searching system. Eventually, the tool should be able to decide where and what to search for based on the users' biography.
- Make a GUI or website for the project in order to make it more accessible. 