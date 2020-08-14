import praw
from langdetect import detect

reddit = praw.Reddit(client_id="L_R7lS48EVgpOA",
                     client_secret="xh7kk4KhkvMyptypb3gEpHm6HfI",
                     password="odl36d5n",
                     user_agent="text scraper",
                     username="KesqiSePasse")

def convertText(text):
    text = text.lower()

    text = text.replace("/", " ")
    text = text.replace("\\", " ")
    text = text.replace("\n", " ")
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("*", " ")
    text = text.replace("&", " ")
    text = text.replace("^", " ")
    text = text.replace("%", " ")
    text = text.replace("$", " ")
    text = text.replace("#", " ")
    text = text.replace("@", " ")
    text = text.replace("*", " ")
    text = text.replace('"', " ")
    text = text.replace('{', " ")
    text = text.replace('}', " ")
    text = text.replace('[', " ")
    text = text.replace(']', " ")
    text = text.replace('<', " ")
    text = text.replace('>', " ")
    text = text.replace('|', " ")
    text = text.replace('`', " ")
    text = text.replace('~', " ")
    text = text.replace("'", "")
    text = text.replace('=', " ")
    text = text.replace('+', " ")

    text_array = []
    fromthis = 0
    for i in range(0, len(text)):
        if text[i] == "!" or text[i] == "?" or text[i] == "." or text[i] == "?" or text[i] == "," or text[i] == ":" or \
                text[i] == ";":
            text_array.append(text[fromthis:i])
            fromthis = i + 1

    file = open("text.txt", "a")

    for z in text_array:
        strarr = []
        removed = []
        for x in z:
            if x.isalnum() or x == " ":
                strarr.append(x)
        z = ""
        for y in strarr:
            z = z + y
        arr = z.split()
        if len(arr) < 2:
            continue
        else:
            for i in range(0, len(arr) - 1):
                this_phrase = arr[i] + " " + arr[i + 1]
                if i == len(arr) - 2:
                    try:
                        file.write(this_phrase + " " + str(end) + "\n")
                    except:
                        pass
                else:
                    try:
                        file.write(this_phrase + " " + arr[i + 2] + "\n")
                    except:
                        pass


end = 857514

for submission in reddit.subreddit("all").stream.submissions():
    if submission.selftext != "":
        text = submission.selftext
        try:
            if detect(text) != "en":
                continue
        except:
            continue

        convertText(text)
        print("submission added")

    for comment in submission.comments:
        if comment.body != "":
            text = comment.body
            try:
                if detect(text) != "en":
                    continue
            except:
                continue

            convertText(text)
            print("comment added")

