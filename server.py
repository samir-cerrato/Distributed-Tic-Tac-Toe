#!/usr/bin/python3
#
# Wesleyan University
# COMP 332
# Homework 2: Distributed tic-tac-toe game

import binascii
import random
import socket
import sys
import threading

from tictactoe import *

class Server():
    """
    Server for TicTacToe game
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.backlog = 1
        self.start()

    def start(self):
        # Init server socket to listen for connections
        try:
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.bind((self.host, self.port))
            server_sock.listen(self.backlog)
        except OSError as e:
            print ("Unable to open server socket: ", e)
            if server_sock:
                server_sock.close()
                sys.exit(1)

        # Wait for client connection
        while True:
            client_conn, client_addr = server_sock.accept()
            print ('Client with address has connected', client_addr)
            thread = threading.Thread(target = self.play, args = (client_conn, client_addr))
            thread.start()

    def play(self, conn, addr):

        # Fill out this function
        # print('Play game here')
        game = TicTacToe(3)  # Create a game 
        game.display("Server")  # Display the  game board

        while not game.check_done():  # Continue playing until game is done
            # Server's turn
            row, col = game.server_choose()  
            game.move(row, col, 'X')  
            game.display("Server")  # Display the updated game board

            # Send the move to the client
            move_str = f"{row},{col}"
            sock_write(conn, move_str)

            if game.check_done():  # Check if server's move resulted in win, loss, or tie
                break

            # Client's turn
            client_move = sock_read(conn)  
            row, col = game.parse_choice(client_move) 
            game.move(row, col, 'O')  
            game.display("Server")  # Display the updated board

        conn.close()  # Close the connection after the game is done 

def main():

    server_host = 'localhost'
    server_port = 50007

    if len(sys.argv) > 1:
        server_host = sys.argv[1]
        server_port = int(sys.argv[2])

    s = Server(server_host, server_port)

if __name__ == '__main__':
    main()
