import Qst
import Ans

class Quiz:

    # arrOfQ = [] #list of all Questions in this quiz

    def __init__(self):
        self.arrOfQ = [] #list of all Questions in this quiz
        self.socialScore = 0
        self.econScore = 0
        self.weightMaxMin = [0, 0, 0, 0]


    def runQuiz(self, filename):

        self.makeQuiz(filename)

        for i in range(len(self.arrOfQ)):
            for w in range(4):
                self.weightMaxMin[w] += self.arrOfQ[i].weight[w]

            currAns = self.arrOfQ[i].askQuestion()

            self.socialScore += currAns.socialScore
            self.econScore += currAns.econScore


    def makeQuiz(self, filename):
        arrQ = []
        #go through social questions
        file = open(filename, "r")
        f_lines = file.readlines()
        currArr = []
        currWeight = []
        for x in f_lines:
            if x[0] == "/":
                currWeight.append(int(x[1:]))
            if x[0] == "-":
                currQ = Qst.Question(x, currArr, currWeight)
                arrQ.append(currQ)
                currArr = []
                currWeight = []
            if x[0] ==":":
                currSoc = int(x[1:])
            if x[0] == ";":
                currEcon = int(x[1:])
            if x[0] == ".":
                currAns = Ans.Answer(x[1:], currSoc, currEcon)
                currArr.append(currAns)


        file.close()

        self.arrOfQ = arrQ
