import a2.isolation as isolation
import a2.test_players as test_players
import submission
import streamlit as st
import pandas as pd


# if st.session_state.clicked == True:
#     # The message and nested widget will remain on the page
#     st.write("("+str(st.session_state.x) + "," +str(st.session_state.y)+")")
# st.write(st.session_state)
def fake_time():
    return 99999

def initialize_game():
    ##create a game
    st.session_state.p1 = test_players.HumanPlayer()
    st.session_state.p2 = submission.CustomPlayer()
    game_board = isolation.Board(st.session_state.p1, st.session_state.p2)
    st.session_state.game = game_board
    # show_board()

def show_board():
    st.header('Game Board')
    board_df = pd.DataFrame(st.session_state.game.get_state())
    st.write(board_df)

def end_game(loser):
    st.title('GAME OVER: '+ loser + ' loses.')


def check_and_make_move(available_moves):
    if (st.session_state.y, st.session_state.x) in available_moves:
        ###forecast move
        new_board, over, winner = st.session_state.game.forecast_move((st.session_state.y, st.session_state.x))

        ###set board to forecasted board
        st.session_state.game.set_state(new_board.get_state(), False)

    else:
        st.write('INVALID MOVE!!!!')
        st.write('You choose (' +str(st.session_state.x)+','+str(st.session_state.y)+')')
        st.write('Valid Available Moves are; '+str(available_moves))

        ##if invalid for now we will just pick the first available move

        new_board, over, winner = st.session_state.game.forecast_move((available_moves[0][0], available_moves[0][1]))
        ###set board to forecasted board
        st.session_state.game.set_state(new_board.get_state(), False)

def submit_move():
    ## PRINT MOVE
    if st.session_state.game_start == False:
        st.session_state.game_start = True
        initialize_game()

    st.write("Submitted Move: (" + str(st.session_state.x) + "," + str(st.session_state.y) + ")")

    ## MAKE MOVE

    ##check if move is legal if not
    available_moves = st.session_state.game.get_player_moves(my_player=st.session_state.p1)

    if len(available_moves) == 0:
        end_game('HUMAN')
        return 1
    else:
        check_and_make_move(available_moves)


    ## MAKE AI MOVE
    available_moves_ai = st.session_state.game.get_player_moves(my_player=st.session_state.p2)

    if len(available_moves_ai) == 0:
        end_game('AI')

    ##get best move
    best_move = st.session_state.p2.move(st.session_state.game, fake_time)

    new_board2, over, winner = st.session_state.game.forecast_move((best_move[0], best_move[1]))
    ###set board to forecasted board
    st.session_state.game.set_state(new_board2.get_state(), True)

    st.write("AI Move: (" + str(best_move[0]) + "," + str(best_move[1]) + ")")

    ## =====END=====






st.title(':european_castle: Welcome to Knights Isolation :european_castle:')
st.write('In this game you play as a knight from a '
         'chess board who is in a duel with another knight. '
         'You may only move as a knight does in chess, and can never move '
         'to a spot that has been visited OR is currently occupied. '
         'You may make one move per turn. The first player to have no available moves on their turn loses.')

st.write('TO-DOs \n' 
         '1. Add sample game board with fixed state that loads under intro paragraph \n'
         '2. On form submit callback function = check valid move THEN conditionally call submit move \n'
         '3. Add game end logic with end game messaging \n'
         '4. Optimize Alpha Beta Pruning for depth 8>')

if 'game_start' not in st.session_state:
    st.session_state.game_start = False

if 'human' not in st.session_state:
    st.session_state.human = True

if st.session_state.human:
    with st.form(key="move_form"):
        st.number_input("Move Column Value (0-8)", 0, 8, key='x')
        st.number_input("Move Row Value (0-8)", 0, 8, key='y')
        st.form_submit_button("Submit Move", on_click=submit_move)

if st.session_state.game_start:
    show_board()