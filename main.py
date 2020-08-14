import random



class markovBot:
    def __init__(self):
        self.end = 857514
        self.markov_dict = [["hello there", "how"], ["there how", "are"], ["how are", "you"], ["are you", self.end],
                       ["hello there", "why"], ["there why", "how"], ["why how", "are"]]

    def run(self):
        while True:
            chat = input()
            chat_lower = chat.lower()

            try:
                start_phrase = chat_lower.split()[0] + " " + chat_lower.split()[1]
            except:
                print("Unable to start, possibly starting sentence too short, at least 2 words.")

            response = start_phrase

            for i in range(0, len(chat_lower.split()) - 1):
                this_phrase = chat_lower.split()[i] + " " + chat_lower.split()[i + 1]
                if i == len(chat_lower.split()) - 2:
                    self.markov_dict.append([this_phrase, self.end])
                else:
                    self.markov_dict.append([this_phrase, chat_lower.split()[i + 2]])

            while True:
                index_array = []
                for index, phrase in enumerate(self.markov_dict):
                    if start_phrase == phrase[0]:
                        index_array.append(index)

                block = self.markov_dict[random.choice(index_array)]
                if block[1] == self.end:
                    break
                response = response + " " + block[1]
                start_phrase_split = start_phrase.split()
                start_phrase = start_phrase_split[1] + " " + block[1]

            print(response)


bot = markovBot()
bot.run()
