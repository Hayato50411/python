#from Rule import G_rule
#from Player import Player
import re

class Player:
    def __init__(self, name, score):
        self.name = name   # Str
        self.score = score # List
        self.total = 0
    
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    def getTotal(self):
        return self.total
    
    def calcTotal(self, course):
        self.total = 0
        for sc, pa in zip(self.score, course.get_par_list()):
            self.total = self.total + (sc - pa)

class Course:   # コースのパーのリストを格納
    def __init__(self):
        self.hole_par = []
    def get_par_list(self): # パーをリストで一括get
        return self.hole_par
    def get_par(self, num): # パーの数を個々でget
        return self.hole_par[num]
    def set_par_list(self, par):
        self.hole_par = par
        
class Judge:    # 勝敗判定
    def judge(self, play1, play2):
        if play1.getTotal() < play2.getTotal() : # player1 Win
            print(play1.getName())
        else :                                   # player2 Win
            print(play2.getName())
        
class Check_input:  # 入力された文字列が指定された文字で構成されているか
    def __init__(self):
        self.pattern = r''

    def check(self, input):
        if re.fullmatch(self.pattern, input):
            print("許可済みの文字で構成")
            return 1
        else :
            print("未許可の文字を検出")
            return 0
    
    def set_pattern(self, pattern):
        self.pattern = pattern

class G_1on1:
    def main_1on1(self):
        print("メイン関数1on1")
        course = Course()
        ch_in = Check_input()
        
        score1 = [] 
        score2 = []

        course.set_par_list([4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4])
        ch_in.set_pattern(r'^[a-zA-Z0-9, ]*$')

        print("選手名1 選手名2 選手1の18コースのスコア 選手2の18コースのスコアを入力")
        while(1):
            str = input()
            if ch_in.check(str) :
                break
            
        str.replace(" ","") 
        name1, name2, score = str.split(",",2)
        sort_score = list(map(int, score.split(",")))

        for i, _ in enumerate(sort_score):
            if i < 18:
                score1.append(sort_score[i])
            else :
                score2.append(sort_score[i])

        print(f"{len(score1)} ホール終了")

        player1 = Player(name1, score1)
        player2 = Player(name2, score2)

        #player1.setTotal(sc1.calc(player1.getScore(), course.get_par_list()))
        #player2.setTotal(sc2.calc(player2.getScore(), course.get_par_list()))
        player1.calcTotal(course)
        player2.calcTotal(course)

        winner = Judge()
        winner.judge(player1, player2)
          
def main():
    g_1on1 = G_1on1()
    #golf = Golf()
    g_1on1.main_1on1()
    
if __name__=="__main__":
    main()

