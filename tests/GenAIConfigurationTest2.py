#%%
import sys
import os

dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/com.xenxsys.genai.projWebCrawlQnA.core/')

print(dir)

sys.path.append(dir)

#%%
import ConfReaderEnv1

#%%
# Establish connection with openai gpt services
dotenv_path="/Users/ajk/Library/CloudStorage/OneDrive-Personal/ajkdrive/codeLab/com.xenexsys.genai.projConf/src/com.xenxsys.genai.projConf.core/.env.production"

client = ConfReaderEnv1.genAIconnection(dotenv_path)

#%%
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system","content":"You are ChatGPT"},
        {"role":"user","content":"who is Sundar Pichai"}
    ]
)

#%%
import textwrap as twrap
print(twrap.fill(completion.choices[0].message.content,150))

# %%
