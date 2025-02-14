
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
#################################################
# file to edit: notebook.ipynb͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑

import time
from a2.isolation import Board

# Credits if any͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
# 1)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
# 2)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
# 3)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑

class OpenMoveEvalFn:
    def score(self, game, my_player=None):
        """Score the current game state
        Evaluation function that outputs a score equal to how many
        moves are open for AI player on the board minus how many moves
        are open for Opponent's player on the board.

        Note:
            If you think of better evaluation function, do it in CustomEvalFn below.

            Args
                game (Board): The board and game state.
                my_player (Player object): This specifies which player you are.

            Returns:
                float: The current state's score. MyMoves-OppMoves.

            """




        return len(game.get_player_moves(my_player)) - len(game.get_opponent_moves(my_player))


######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
################ END OF LOCAL TEST CODE SECTION ######################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑

class CustomPlayer:
    # TODO: finish this class!͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
    """Player that chooses a move using your evaluation function
    and a minimax algorithm with alpha-beta pruning.
    You must finish and test this player to make sure it properly
    uses minimax and alpha-beta to return a good move."""

    def __init__(self, search_depth=5, eval_fn=OpenMoveEvalFn()):
        """Initializes your player.

        if you find yourself with a superior eval function, update the default
        value of `eval_fn` to `CustomEvalFn()`

        Args:
            search_depth (int): The depth to which your agent will search
            eval_fn (function): Evaluation function used by your agent
        """
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, time_left):
        """Called to determine one move by your agent

        Note:
            1. Do NOT change the name of this 'move' function. We are going to call
            this function directly.
            2. Call alphabeta instead of minimax once implemented.
        Args:
            game (Board): The board and game state.
            time_left (function): Used to determine time left before timeout

        Returns:
            tuple: (int,int): Your best move
        """
        best_move, utility = alphabeta(self, game, time_left, depth=self.search_depth)
#         print(game.print_board())
#         print("Move Chosen",best_move)
#         print("Utility", utility)
        return best_move



    def utility(self, game, my_turn):
        """You can handle special cases here (e.g. endgame)"""

        return self.eval_fn.score(game, self)



###################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE CLASS! ################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
###### IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ###########͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
###################################################################



def minimax(player, game, time_left, depth, my_turn=True, over=False):
    """Implementation of the minimax algorithm.
    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you
            need from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer()).
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """




##Without recursion???
        ##build game tree at correct depth
        #### for i in range depth
        ####    if my_turn then k1 = depth % 2 and k2 = depth % 2 + 1
        ####    get avail moves and for each move
        ####    forecast board and score utility
        ####.   repeat X times for depth then stop
        ##Explore game tree and select moves
        #### for i in range depth
        ####    make decision for k1 then k2


        ##NEED TO MAKE COMPARISON BETWEEN UTILITIES

    if my_turn:

        if depth == 0 or over == True:

            return (None, player.utility(game, my_turn))

        util = -9999
        available_moves = game.get_player_moves(player)
#         random.shuffle(available_moves)
        depth = depth-1
        print('at depth', depth)
        stored_moves = []
        for move in available_moves:
            forecasted_board, is_over, winner = game.forecast_move(move)

            print('what would min do if we made move:', move)

            new_move, new_util = minimax(player, forecasted_board, time_left, depth, my_turn=False, over=is_over)

#             print('if max made move:'+ str(move)+' its utility for us would be'+str(new_util))
            best_move = (move,new_util)
            stored_moves.append(best_move)

        ##get move with largest utility
        sorted_moves = sorted(stored_moves, key=lambda item: item[1], reverse=True)

#         print("sorted_moves first", sorted_moves)
#         print("stored_moves first", stored_moves)

        return sorted_moves[0][0], sorted_moves[0][1]

    else:

        if depth == 0 or over == True:

            return (None, player.utility(game, my_turn))

        util = 9999
        available_moves = game.get_opponent_moves(player)
#         random.shuffle(available_moves)
        depth = depth-1
        print('at depth', depth)
        stored_moves = []
        for move in available_moves:

            forecasted_board, is_over, winner = game.forecast_move(move)

#             print('what would max do if we made move:', move)
            new_move, new_util = minimax(player, forecasted_board, time_left, depth, my_turn=True, over=is_over)
#             print('if min made move:'+ str(move)+' its utility for us would be'+str(new_util))

            best_move = (move,new_util)
            stored_moves.append(best_move)

        sorted_moves = sorted(stored_moves, key=lambda item: item[1])


#         print("sorted_moves first", sorted_moves)
#         print("stored_moves first", stored_moves)


        print('returing value', best_move)
        return sorted_moves[0][0], sorted_moves[0][1]




#

######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
# tests.beatRandom(CustomPlayer)
################ END OF LOCAL TEST CODE SECTION ######################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑

def alphabeta(player, game, time_left, depth, alpha=float("-inf"), beta=float("inf"), my_turn=True, over=False):
    """Implementation of the alphabeta algorithm.

    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you need
            from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer())
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        alpha (float): Alpha value for pruning
        beta (float): Beta value for pruning
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """

##Decide Turn

    if my_turn:

##Check Termination Conditions: Depth=0 | Game is over | Time left is approaching 0
        if depth == 0 or over == True or time_left()<=100:

            return (None, player.utility(game, my_turn))

##If we don't terminate begin evaluating moves
        util = -9999
        available_moves = game.get_player_moves(player)

        depth = depth-1
#         print('at depth', depth)
        stored_moves = []

##For each move ask "what would min do?" by calling minimax again with the forecasted board
        for move in available_moves:
            forecasted_board, is_over, winner = game.forecast_move(move)

            sorted_moves = sorted(stored_moves, key=lambda item: item[1], reverse=True)

#             print('what would min do if we made move:', move)
#             print("stored moves before function call", sorted_moves)

##If we have no stored moves yet (still exploring the first max depth branch then beta = inf else beta = best discovered move)
            if len(sorted_moves) >0:
                b=sorted_moves[0][1]
            else:
                b=beta

            new_move, new_util = alphabeta(player, forecasted_board, time_left, depth, my_turn=False, over=is_over, alpha=alpha,beta=b)

            best_move = (move,new_util)
            stored_moves.append(best_move)
#             print('if max made move:'+ str(move)+' its utility for us would be'+str(new_util))

##If the utility found for the move is > than alpha then we prune (except when alpha is still default val)

            if new_util > alpha and alpha != float("-inf"):
#                 print("New Util discoverd for move" + str(new_move) + str(new_util)+ " is greater than alpha of:" +str(alpha))
                break

#             print("Max: Just explored new_move stored moves so far are"+ str(new_move) + str(new_util))
#             print("stored moves", stored_moves)

##Sort and return move with best utility discovered
        sorted_moves = sorted(stored_moves, key=lambda item: item[1], reverse=True)

#         print("sorted_moves first", sorted_moves)
#         print("stored_moves first", stored_moves)
#         print('returing value move', sorted_moves[0][0])
#         print('returing value util', sorted_moves[0][1])
        return sorted_moves[0][0], sorted_moves[0][1]

    else:

        if depth == 0 or over == True or time_left()<=100:

            return (None, player.utility(game, my_turn))

        util = 9999
        available_moves = game.get_opponent_moves(player)

        depth = depth-1
#         print('at depth', depth)
        stored_moves = []
        for move in available_moves:

            forecasted_board, is_over, winner = game.forecast_move(move)

            sorted_moves = sorted(stored_moves, key=lambda item: item[1])

#             print("stored moves before function call", sorted_moves)

#             print('what would max do if we made move:', move)

            if len(sorted_moves) >0:
                a=sorted_moves[0][1]
            else:
                a=alpha

            new_move, new_util = alphabeta(player, forecasted_board, time_left, depth, my_turn=True, over=is_over, alpha=a, beta=beta)
#             print('if min made move:'+ str(move)+' its utility for us would be'+str(new_util))

            best_move = (move,new_util)
            stored_moves.append(best_move)

            if new_util < beta and beta != float("inf"):
#                 print("New Util discoverd for move" + str(new_move) + str(new_util)+ " is less than beta of:" +str(beta))
                break

#             print("Min: Just explored new_move stored moves so far are" + str(new_move) + str(new_util))
#             print("stored moves", stored_moves)

        sorted_moves = sorted(stored_moves, key=lambda item: item[1])


#         print("sorted_moves first", sorted_moves)
#         print("stored_moves first", stored_moves)


#         print('returing value move', sorted_moves[0][0])
#         print('returing value util', sorted_moves[0][1])
        return sorted_moves[0][0], sorted_moves[0][1]


######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE FUNCTION! ################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######################################################################
##### CODE BELOW IS USED FOR RUNNING LOCAL TEST DON'T MODIFY IT ######͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
################ END OF LOCAL TEST CODE SECTION ######################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑

class CustomEvalFn:
    def __init__(self):
        pass

    def score(self, game, my_player=None):
        """Score the current game state.

        Custom evaluation function that acts however you think it should. This
        is not required but highly encouraged if you want to build the best
        AI possible.

        Args:
            game (Board): The board and game state.
            my_player (Player object): This specifies which player you are.

        Returns:
            float: The current state's score, based on your own heuristic.
        """

        # TODO: finish this function!͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑


        raise NotImplementedError

######################################################################
############ DON'T WRITE ANY CODE OUTSIDE THE CLASS! #################͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏︀͏󠄍͏󠄑
######################################################################