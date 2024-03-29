#%%
import sys
import os
dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/src/com.xenxsys.genai.projWebCrawlQnA.core/')

print(dir)
sys.path.append(dir)

#%%
import ConfReaderJson1 as ConfReader
from openai import OpenAI

# %%
#change location of conf.json
conf_json_location = "/Users/ajk/Library/CloudStorage/OneDrive-Personal/ajkdrive/codeLab/com.xenexsys.genai.projConf/src/com.xenxsys.genai.projConf.core/conf.json"
ConfReaderKeyValue = ConfReader.Config.load_json(conf_json_location)

client = OpenAI(api_key = ConfReaderKeyValue.openai_api_key_1)
print("Connection is successful")
# %%
completion = client.chat.completions.create(
    model= ConfReaderKeyValue.GPTmodel1,
    messages=[
        {"role":"system","content":"your are a GPT model"},
        {"role":"user","content":"What is GPT"}
    ]
)
#%%
import textwrap as twrap

print("This is openai communication test: communication successful\n\n")

print(twrap.fill(completion.choices[0].message.content,150)+"\n\n")

# %%
