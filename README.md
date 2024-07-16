# situational-awareness
A tool to aggregate information on specific topics for researchers and professionals.

Papers from relevant topics published within a specified number of days are queried from the arxiv. The information, along with the user's provided background, is then passed to a Google Gemini model. The Gemini model returns a summary relevant to the user's background. 

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
- Run the main file, and check the output directory!

Contact me (afs223@cornell.edu) in the event of an error or with suggestions for improving this tool. 


## Next Steps in Development 

- Integrate Perplexity search for more general news/information. 
- Make a GUI or website (probably Django) for the project in order to make it more accessible. 
