import markovify

# Get raw text as string.


<<<<<<< HEAD
def create_markov_model(text_input):
    #with open("DownloadedTweets.txt") as f:
    #   text = f.read()
    # Build the model.
    text_model = markovify.Text(text_input)
    #print(text)
    pred = text_model.make_short_sentence(140)
    #print(pred)
    return pred
=======
def create_markov_model():
    with open("DownloadedTweets.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    return text_model.make_short_sentence(140)
>>>>>>> ecd4c36603aeb78b6c3f6cd26b20599afe3933b3
