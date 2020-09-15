import Qst
import Quiz

def main():


    exQuiz = Quiz.Quiz()
    exQuiz.runQuiz("QuestionsText.txt")
    print("Social Score: " + str(exQuiz.socialScore))
    print("Econ Score: " + str(exQuiz.econScore))

    socialPercent = round(float(exQuiz.socialScore + (-1 * exQuiz.weightMaxMin[0]))/float(exQuiz.weightMaxMin[1] + (-1 * exQuiz.weightMaxMin[0])), 2)
    econPercent = round(float(exQuiz.econScore + (-1 * exQuiz.weightMaxMin[2]))/float(exQuiz.weightMaxMin[3] + (-1 * exQuiz.weightMaxMin[2])), 2)

    print("Social Score: " + str(socialPercent))
    print("Economic Score: " + str(econPercent))


    createGraph(16, socialPercent, econPercent)

    # print("\nMin Social Score: " + str(exQuiz.weightMaxMin[0]))
    # print("\nMax Social Score: " + str(exQuiz.weightMaxMin[1]))
    # print("\nMin Econ Score: " + str(exQuiz.weightMaxMin[2]))
    # print("\nMax Econ Score: " + str(exQuiz.weightMaxMin[3]))

    # social10 = int(socialPercent*10)
    # if social10 == 10:
    #     social10 = 9
    # econ10 = int(econPercent*10)
    # if econ10 == 10:
    #     econ10 = 9
    # for y in range(10):
    #     if y == 5:
    #         print("-------------------------------")
    #     for x in range(10):
    #         if x == 5:
    #             print("|  ", end="")
    #
    #         if(((9 - y) == social10) & (x == econ10)):
    #             print("O  ", end="")
    #         else:
    #             print(".  ", end="")
    #     print()


def createGraph(n, socialPercent, econPercent):
    social10 = int(socialPercent*n)
    if social10 == n:
        social10 = n-1
    econ10 = int(econPercent*n)
    if econ10 == n:
        econ10 = n-1
    for y in range(n):
        if y == n/2:
            for i in range(int(n*3/2 +1)):
                print("- ", end="")
            print()
        for x in range(n):
            if x == n/2:
                print("|  ", end="")

            if(((n-1 - y) == social10) & (x == econ10)):
                print("O  ", end="")
            else:
                print(".  ", end="")
        print()



main()
