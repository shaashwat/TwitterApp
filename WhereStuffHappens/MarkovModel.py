import markovify

# Get raw text as string.


def create_markov_model(text_input):
    #with open("DownloadedTweets.txt") as f:
    #   text = f.read()
    # Build the model.
    text_model = markovify.Text(text_input)
    #print(text)
    pred = text_model.make_short_sentence(140)
    #print(pred)
    return pred
