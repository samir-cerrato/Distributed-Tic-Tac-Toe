#!/usr/bin/python3
#
# Wesleyan University
# COMP 332
# Homework 2: Distributed tic-tac-toe game

import binascii
import random
import socket
import sys

from tictactoe import *

class Client:

    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.start()

    def start(self):

        # Fill this out
        # print("start game")
        # Establish connection with the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.server_host, self.server_port))
            self.play(sock)

    def play(self, sock):

        # Fill this out
        # print("play game")
        game = TicTacToe(3)  # Create a game 
        game.display("Client")  # Display the initial game board

        while not game.check_done():  # Continue playing until game is tied or there is a winner
            # Server's turn and display their move
            server_move = sock_read(sock)  
            row, col = game.parse_choice(server_move)
            game.move(row, col, 'X')  
            game.display("Client")

            # Check if server's move resulted in win, loss, or tie
            if game.check_done():  
                break

            # Client's turn and display the updated board
            row, col = game.user_choose()  
            game.move(row, col, 'O')  
            game.display("Client")

            # Send the move to the server
            move_str = f"{row},{col}"
            sock_write(sock, move_str)

        sock.close()  # Close the connection after the game is done

def main():
    server_host = 'localhost'
    server_port = 50007

    if len(sys.argv) > 1:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])

    client = Client(server_host, server_port)

if __name__ == '__main__':
    main()
