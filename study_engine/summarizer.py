# Summarizer module for the AI Study Tool
import os
#reads API key from environmental variables

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def ai_summarize_text(text):
    ''' Takes in a string of text and returns 
    a max  high-level 300 character summary. 
    Optimized for students wanting to quickly grasp their notes
    at a high level.
    '''
    return ("Summary generation not yet implemented. ")
