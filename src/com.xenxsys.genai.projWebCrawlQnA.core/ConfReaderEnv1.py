#%%
import os
from dotenv import load_dotenv
from openai import OpenAI
#%%
__name__ = "ConfReaderEnv1"
#%%
# Load environment variables from .env file
def genAIconnection(dotenv_path):
    load_dotenv(dotenv_path)

    api_key_1 = os.environ['API_KEY_1']
  
    print("Connection successful...")

    return OpenAI( api_key = api_key_1)

# %%
