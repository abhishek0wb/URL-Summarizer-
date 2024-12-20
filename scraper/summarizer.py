from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_path = "./model"

# Automatically download the model if not present
summarizer = pipeline(
    "summarization",
    model=AutoModelForSeq2SeqLM.from_pretrained("t5-small"),
    tokenizer=AutoTokenizer.from_pretrained("t5-small"),
)

def summarize_text(content):
    try:
        input_text = content[:512]  # Limit input length
        summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Failed to generate summary."
