from collections import defaultdict

class AhoCorasick:
    def __init__(self, words):
 
        self.max_states = sum([len(word) for word in words])

        self.max_characters = 26
 

        self.out = [0]*(self.max_states+1)
 
        self.fail = [-1]*(self.max_states+1)

        self.goto = [[-1]*self.max_characters for _ in range(self.max_states+1)]

        for i in range(len(words)):
          words[i] = words[i].lower()
        self.words = words
        self.states_count = self.__build_matching_machine()
 
    def __build_matching_machine(self):
        k = len(self.words)
 
        states = 1
 
        for i in range(k):
            word = self.words[i]
            current_state = 0

            for character in word:
                ch = ord(character) - 97 
 
                if self.goto[current_state][ch] == -1:
                    self.goto[current_state][ch] = states
                    states += 1
 
                current_state = self.goto[current_state][ch]

            self.out[current_state] |= (1<<i)

        for ch in range(self.max_characters):
            if self.goto[0][ch] == -1:
                self.goto[0][ch] = 0

        queue = []
        for ch in range(self.max_characters):
            if self.goto[0][ch] != 0:
                self.fail[self.goto[0][ch]] = 0
                queue.append(self.goto[0][ch])
        while queue:
            state = queue.pop(0)
            for ch in range(self.max_characters):

                if self.goto[state][ch] != -1:
                    failure = self.fail[state]

                    while self.goto[failure][ch] == -1:
                        failure = self.fail[failure]
                     
                    failure = self.goto[failure][ch]
                    self.fail[self.goto[state][ch]] = failure

                    self.out[self.goto[state][ch]] |= self.out[failure]

                    queue.append(self.goto[state][ch])
         
        return states
 
    def __find_next_state(self, current_state, next_input):
        answer = current_state
        ch = ord(next_input) - 97 # Ascii value of 'a' is 97
 
        # If goto is not defined, use
        # failure function
        while self.goto[answer][ch] == -1:
            answer = self.fail[answer]
 
        return self.goto[answer][ch]

    def search_words(self, text):
        text = text.lower()
        current_state = 0
        result = defaultdict(list)
        for i in range(len(text)):
            current_state = self.__find_next_state(current_state, text[i])
            if self.out[current_state] == 0: continue
            for j in range(len(self.words)):
                if (self.out[current_state] & (1<<j)) > 0:
                    word = self.words[j]
                    result[word].append(i-len(word)+1)
        return result


"""
if __name__ == "__main__":
    words = ["he", "she", "hers", "his"]
    text = "ahishers"
 
    aho_chorasick = AhoCorasick(words)

    result = aho_chorasick.search_words(text)

    for word in result:
        for i in result[word]:
            print("Word", word, "appears from", i, "to", i+len(word)-1)
"""