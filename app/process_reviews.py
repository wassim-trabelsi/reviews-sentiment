import transformers
import nltk

classifier = transformers.pipeline('sentiment-analysis', model = "distilbert-base-uncased-finetuned-sst-2-english")

def positivity_score(sentence):
    sign = 1 if classifier(sentence)[0]["label"] == "POSITIVE" else -1
    return classifier(sentence)[0]["score"] * sign

def process_reviews(reviews):
    """Get reviews from the API"""
    all_sentences = []
    for review in reviews:
        for sentence in nltk.tokenize.sent_tokenize(review.replace(' -', ' .').replace(',', '.').replace(':', '.')):
            all_sentences.append(sentence)
    

    sentence_scores = [{"feedback":sentence, "score": positivity_score(sentence)**41} for sentence in all_sentences]
    sentence_scores.sort(key=lambda x: x["score"], reverse=True)

    return sentence_scores

if __name__ == "__main__":
    reviews = [ "I love this movie", "I hate this movie", "I don't know what to think about this movie"]
    print(process_reviews(reviews))
