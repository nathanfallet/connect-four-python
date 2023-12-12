from queue import Queue
from threading import Thread

from ai import *
from board import *


class Connect4:

    def __init__(self):
        self.board = Board()
        self.human_turn = False
        self.turn = 1
        self.players = (0, 0)
        self.ai_move = Queue()

    def current_player(self):
        return 2 - (self.turn % 2)

    def launch(self, window, information, combobox_player1, combobox_player2, canvas1):
        self.board.reinit(canvas1)
        self.turn = 0
        information['fg'] = 'black'
        information['text'] = "Turn " + str(self.turn) + " - Player " + str(
            self.current_player()) + " is playing"
        self.human_turn = False
        self.players = (combobox_player1.current(), combobox_player2.current())
        self.handle_turn(window, information, canvas1)

    def move(self, column, window, information, canvas1):
        if not self.board.column_filled(column):
            self.board.add_disk(column, self.current_player(), canvas1)
            self.handle_turn(window, information, canvas1)

    def click(self, event, window, information, canvas1):
        if self.human_turn:
            column = event.x // row_width
            self.move(column, window, information, canvas1)

    def ai_turn(self, ai_level, window, information, canvas1):
        Thread(target=alpha_beta_decision,
               args=(self.board, self.turn, ai_level, self.ai_move, self.current_player())).start()
        self.ai_wait_for_move(window, information, canvas1)

    def ai_wait_for_move(self, window, information, canvas1):
        if not self.ai_move.empty():
            self.move(self.ai_move.get(), window, information, canvas1)
        else:
            window.after(100, self.ai_wait_for_move, window, information, canvas1)

    def handle_turn(self, window, information, canvas1):
        self.human_turn = False
        if self.board.check_victory():
            information['fg'] = 'red'
            information['text'] = "Player " + str(self.current_player()) + " wins !"
            return
        elif self.turn >= 42:
            information['fg'] = 'red'
            information['text'] = "This a draw !"
            return
        self.turn = self.turn + 1
        information['text'] = "Turn " + str(self.turn) + " - Player " + str(
            self.current_player()) + " is playing"
        if self.players[self.current_player() - 1] != 0:
            self.human_turn = False
            self.ai_turn(self.players[self.current_player() - 1], window, information, canvas1)
        else:
            self.human_turn = True
