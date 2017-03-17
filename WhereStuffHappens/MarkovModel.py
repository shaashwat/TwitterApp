import markovify

# Get raw text as string.


def create_markov_model():
    with open("DownloadedTweets.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)
    #print(text)
    pred = text_model.make_short_sentence(140)
    #print(pred)
    return pred
