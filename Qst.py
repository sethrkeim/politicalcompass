class Question:

    selected = -1

    def __init__(self, qst, answers, weight):
        self.qst = qst
        self.answers = answers #list of answer objects
        self.weight = weight # [socMin, socMax, econMin, econMax]

    def askQuestion(self):
        done = False
        while not done:
            print(self.qst)
            for i in range(len(self.answers)):
                print("(" + str(i+1) + ")  " + self.answers[i].text)
            try:
                response = int(input())
                if 1 <= responseas <= len(self.answers):
                    done = True
                else:
                    print("Invalid response")
                    print()
            except:
                print("Must type an integer")
                print()

        for i in range(len(self.answers)):
            if response == (i+1):
                self.selected = self.answers[i]
        print()
        return self.selected #Answer object that was selected
