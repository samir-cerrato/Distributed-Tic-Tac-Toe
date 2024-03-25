# Distributed-Tic-Tac-Toe
Make the tic-tac-toe game a distributed application using socket programming.

Your goal is to implement a distributed version of tic-tac-
toe. Some starter code has been provided for you:

•tictactoe.py: This file contains two classes: Board and TicTacToe. If you’d like to use
your own tic-tac-toe game code, you are free to, but you should still put it in a file called
tictactoe.py that does not contain any main.

Any functions or methods you would like to share across the server and client, you should
add to tictactoe.py and then call them from the server or client. For instance, you may
wish to add functions to parse the strings sent or received by the client or server. If your
code is organized well, the same TicTacToe class should be useable by either the central-
ized or distributed versions of the game, just by changing the client and server code.

•server.py: This file contains the tic-tac-toe server code. Method stubs have been imple-
mented for you to get you started. The primary method that you will need to fill out is
the play method, although you may want implement additional helper methods. As before
the server will still query the client (as well as choose its own strategy to play), however,
any information exchanged between the client and server will be sent and received from a
socket.

The server is multi-threaded. This means that rather than blocking on a client while
that client is being served, a thread is spawned off the main thread of execution of the
server process to serve each client that connects to the server. This lets the main execution
thread of the server continue to listen for new client connections, while clients are being
served. If multiple clients connect to the server simultaneously, then each would be served
without blocking the other. You should not need to modify the threading code. As an
aside, Python does not have true multi-threading in that the use of threads will actually
make the code run slower rather than faster (e.g., because separate threads cannot run in
parallel on separate cores). The benefit of threading here is that it allows for a simpler
server implementation.

•client.py: function stubs have been implemented for you to get you started. You’ll want
to have the client first create a connection with the server (via a socket), and then have
the client send and receive (binary) data from the socket in order to communicate with the
server.
