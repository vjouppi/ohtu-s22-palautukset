class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points = self.player1_points + 1
        if player_name == self.player2_name:
            self.player2_points = self.player2_points + 1

    def endgame_points_to_text(self, points1, points2):
        points_difference = points1 - points2

        if points_difference == 1:
            return("Advantage " + self.player1_name)
        elif points_difference == -1:
            return("Advantage " + self.player2_name)
        elif points_difference >= 2:
            return("Win for " + self.player1_name)
        else:
            return("Win for " + self.player2_name)

    def points_to_text(self, points):
        if points == 0:
            return("Love")
        elif points == 1:
            return("Fifteen")
        elif points == 2:
            return("Thirty")
        elif points == 3:
            return("Forty")

    def tied_points_to_text(self, points):
        if points >= 4:
            return("Deuce")
        else:
            return(self.points_to_text(points) + "-All")

    def get_score(self):
        if self.player1_points == self.player2_points:
            return(self.tied_points_to_text(self.player1_points))
        elif self.player1_points >= 4 or self.player2_points >= 4:
            return(self.endgame_points_to_text(self.player1_points, self.player2_points))
        else:
            player1_score = self.points_to_text(self.player1_points)
            player2_score = self.points_to_text(self.player2_points)
            return(player1_score + "-" + player2_score)
