

class WordTracker():
    outofplace = {}
    absoluteword = {0: "", 1: "", 2: "", 3: "", 4: ""}

    def __init__(self, filename="words", wordlist=[]):
        if wordlist:
            self.initialword = wordlist.copy()
        else:
            with open(filename) as fp:
                self.initialword = fp.read().splitlines()
        self.currentlyknown = [
            'abcdefghijklmnopqrstuvwxyz',
            'abcdefghijklmnopqrstuvwxyz',
            'abcdefghijklmnopqrstuvwxyz',
            'abcdefghijklmnopqrstuvwxyz',
            'abcdefghijklmnopqrstuvwxyz',
        ]
        self.validwords = self.initialword.copy()

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            self.outofplace[letter] = [0, 1, 2, 3, 4]

    def get_status(self):
        return {
            "initial": len(self.initialword),
            "current": len(self.validwords)
        }

    def get_current_list(self):
        return self.validwords

    def get_current_list_length(self):
        return len(self.validwords)

    def update_knowledge(self, word, result, debug=True):
        for i in range(5):
            if result[i] == 2:
                self.currentlyknown[i] = word[i]
                self.absoluteword[i] = word[i]
                # That's the easy bit - the tricky part is validating
                # if the letter appears again in the word.
                for entry in self.outofplace:
                    if entry != word[i]:
                        if i in self.outofplace[entry]:
                            self.outofplace[entry].remove(i)

            if result[i] == 1:
                self.currentlyknown[i] = self.currentlyknown[i].replace(word[i], "")
                if i in self.outofplace[word[i]]:
                    self.outofplace[word[i]].remove(i)

            if result[i] == 0:
                if word.count(word[i]) == 1:
                    for j in range(5):
                        self.currentlyknown[j] = self.currentlyknown[j].replace(word[i], "")

        self.calculate_validwords()

    def calculate_validwords(self):
        self.validwords = []
        for word in self.initialword:
            valid = True
            for i in range(5):
                if word[i] not in self.currentlyknown[i]:
                    valid = False
                if i not in self.outofplace[word[i]]:
                    valid = False
            if valid:
                self.validwords.append(word)








