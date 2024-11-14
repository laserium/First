import openai
from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("training_data_chat_added.jsonl", "rb"),
  purpose="fine-tune"
)
print ("done")