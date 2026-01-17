from cleaning import clean
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
"microsoft/Phi-3-mini-4k-instruct",
device_map="cpu",
torch_dtype="auto",
trust_remote_code=False,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
enc = tokenizer(prompt, return_tensors="pt")

input_ids = enc["input_ids"].to("cpu")
attention_mask = enc["attention_mask"].to("cpu")

generation_output = model.generate(
    input_ids=input_ids,
    attention_mask=attention_mask,
    max_new_tokens=200,
)
