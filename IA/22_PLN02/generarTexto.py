from transformers import pipeline

gpt2_generator = pipeline('text-generation', model='gpt2')

sentences = gpt2_generator("Artificial Intelligence is changing the world because", do_sample=True, top_k=50, temperature=0.7, max_length=128, num_return_sequences=1)

for sentence in sentences:
    print("="*50)
    print(sentence["generated_text"])
    print("="*50)