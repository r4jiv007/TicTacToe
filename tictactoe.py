"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    function to run monte-carlo trial
    """
    empty = board.get_empty_squares()
    index = random.randint(0,len(empty)-1)
    pmove=empty[index]
    currp=player
    board.move(pmove[0],pmove[1],currp)
    while True:
        if board.check_win() != None:
            break
        else:
            empty = board.get_empty_squares()
            index = random.randint(0,len(empty)-1)
            pmove=empty[index]
            currp=provided.switch_player(currp)
            board.move(pmove[0],pmove[1],currp)
            
def mc_update_scores(scores, board, player):
    """
    function to update the scores
    """
    winner = board.check_win()
    dim = board.get_dim()
    for row in range(dim):
        for col in range(dim):
            if board.square(row,col) == provided.EMPTY or winner == provided.DRAW:
                scores[row][col] += 0
            elif board.square(row,col) == winner:
                scores[row][col] += SCORE_CURRENT
            else:
                scores[row][col] -= SCORE_OTHER
    
    

def get_best_move(board, scores):
    """
    method to return the best move according to the score
    """
    empty_cells = board.get_empty_squares()
    score_list = list()
    for cell in empty_cells:
        score_list.append(scores[cell[0]][cell[1]])
    max_score = max(score_list)
    max_score_list = list()
    for cell in range(len(empty_cells)):
        square = (empty_cells[cell])
        if scores[square[0]][square[1]] == max_score:
            max_score_list.append((square[0],square[1]))
    if len(max_score_list)>0:
        index = random.randint(0,len(max_score_list)-1)
        return max_score_list[index]
    else:
        return max_score_list[0]


def mc_move(board, player, trials):
    """
    function to make move
    """
    dim = board.get_dim()
    myscores = [[0 for dummy_col in range(dim)]for dummy_row in range(dim)]
    for dummy_trial in range(trials):
        myboard= board.clone()
        mc_trial(myboard,player)
        mc_update_scores(myscores,myboard,player)
    my_move = get_best_move(board,myscores)
    return my_move

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

