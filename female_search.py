import pprint

import requests


def fetch_json(url):
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    female_search_url = "https://ws.spraakbanken.gu.se/ws/korp/v8/query?default_context=1 sentence&start=0&end=15000&corpus=ATTASIDOR&cqp=[lemma contains \".*?kvinn.*\"]&incremental=true&default_within=sentence"
    data = fetch_json(female_search_url)
    stop_words = fetch_json("https://raw.githubusercontent.com/stopwords-iso/stopwords-sv/master/stopwords-sv.json")

    word_frequencies = {}
    for sentence in data["kwic"]:
        for token in sentence["tokens"]:
            word = token["word"].lower()
            if not word.isalpha() or word in stop_words:
                continue
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    top_word_amount = min(30, len(word_frequencies))
    top_most_frequent = sorted(
        [(token, frequency) for token, frequency in word_frequencies.items()],
        key=lambda x: x[1],
        reverse=True)[:top_word_amount]

    pprint.pprint(top_most_frequent)