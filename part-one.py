import torch
from cleaning import clean
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

book = str(input("Enter the book name: "))
full_data = clean(book)
data = full_data[:300]

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="cpu",
    torch_dtype=torch.float32,
    trust_remote_code=False
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=50,
    do_sample=False,
    temperature=0.7
)

prompt = f"Summarize the following text: {data}"

output = generator(prompt)
print(output[0]['generated_text'])
