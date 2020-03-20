<h1 align="center">Welcome to online TicTacToe game 👋</h1>
<p>
  <a href="https://www.python.org/"><img alt="Python version: 3.x" src="https://img.shields.io/badge/python-python%203.x-blue.svg">
  </a>
  <a href="https://github.com/HadiZakiAlQattan/sudoku/blob/master/LICENSE" target="_blank">  
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://docutils.sourceforge.io/rst.html"><img alt="Docstrings: reStructuredText" src="https://img.shields.io/badge/docstrings-reStructuredText-gree.svg">
  </a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
</p>

> online-tictactoe is a GUI online pygame version of tictactoe game with AI, created using socket lib for server-side and client network.

<br>

# Online-TicTacToe ([Client](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client))

> Online-tictactoe client is a client-side part of online-tictactoe game using python pygame lib aim to make a wonderful GUI for tictactoe game with simple network using socket and pickle lib.

# Usage 🗝

There are two ways to use the client side :

* Using exe version without any requirements :
    * Download entire exe dir.
    * Configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/exe/server.yaml) file (set server host & port).
    * Run exe/[main.exe](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/exe/main.exe).
    * Start playing!

        ![ttt-interface](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/init.jpg?raw=true)

* Using [runner.sh](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/runner.sh) :
    
    * Install requirements : 
        ```shell
        $ sudo pip3 install -r requirements.txt
        ```
    * Run the game : 
        ```shell 
        $ ./runner.sh g
        ```
    * Start playing!
    
        ![ttt-interface](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/init.jpg?raw=true)

# Demo  🧮
> You can playing with any connected enemy or playing with AI.

# Play Online (online)

## Start the server to start playing
* configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/server.yaml) file for client.
* start the server.
    
    ![start-the-server](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/start_server.gif?raw=true)

## Start playing with stable connection!
* choose empty square using (mouse/keyboard).
* hit enter to set a value.
* wherever you play, your enemy will see the result immediately.
    
    ![state-share](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/state_share.gif?raw=true)

## Winning / Losing cases
* the game will reseted.
* your symbol will changed.

    ![win-lose-cases](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/end_edge.gif?raw=true)

# Play With AI (offline & online)

## Change from online mode to AI mode
* press 'Play With AI' button.
* game will reseted and connection will not recv any data. 
* there are four AI engine levels :
    * the level will automatically increased when you win.
    * maximum level is 4.
    * after each game you'll get a new playing symbol.
    
        ![change-to-ai-mode](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/setaimode.gif?raw=true)

## Set value and get AI response
* choose empty square using (mouse/keyboard). 
* hit enter to set a value. 
* you'll get an AI response.
    
    ![ai-res](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/ai_res.gif?raw=true)

## Winning case
* AI engine level will increased.
* the game will reseted.
* your symbol will changed.
    
    ![win](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/win.gif?raw=true)

## Losing case 
* AI engine level will not increased. 
* the game will reseted. 
* your symbol will changed.
    
    ![lose](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/lose.gif?raw=true)

# Tests 🧪

Test dir include tests for two classes :
* [network.network.Network](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/src/network/network.py)
* [tictactoe.tictactoe.TicTacToe](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/src/tictactoe/tictactoe.py) (only whoWinner function)
* [tictactoe.tictactoe.TicTacToe](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/src/tictactoe/tictactoe.py) (entire class)

### Run instructions :
* Install requirements:
    ```shell
    $ sudo pip3 install -r requirements.txt
    ```
* All tests : 
    * Run all tests using [runner.sh](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/runner.sh)
        ```shell
        $ ./runner.sh t
        ```
    * [network.network.Network](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/src/network/network.py) class : 
        ```shell
        $ ./runner.sh tn
        ```
    * [tictactoe.tictactoe.TicTacToe](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/src/tictactoe/tictactoe.py) (only whoWinner function) : 
        ```shell
        $ ./runner.sh tt
        ```
    * [tictactoe.tictactoe.TicTacToe](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/src/tictactoe/tictactoe.py) (entire class) : 
        ```shell
        $ ./runner.sh ta
        ```

<br>

# Online-TicTacToe ([Server](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server))

> Online-tictactoe server is a server-side part of online-tictactoe game using python socket lib and pickle lib aim to make a stable connection between two threaded tictactoe players and send/recv data from/to players as objects using pickle lib.

# Usage 🗝

There are two ways to use the server :

* Using exe version without any requirements :
    * Download entire exe dir
    * Configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/exe/server.yaml) file (set server host & port)
    * Run exe/[main.exe](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/exe/main.exe)
    * Press start button
   
        ![server gui jpg](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/docs/server_gui.jpg?raw=true)

* Using [runner.sh](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/runner.sh) and there are three ways:  
    
    * Inside your machine (both CLI & GUI) :
        * Install requirements: 
            ```shell
            $ sudo pip3 install -r requirements.txt
            ```
        * Configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/server.yaml) file (set server host & port)
        * CLI : 
            ```shell 
            $ ./runner.sh c
            ```
        * GUI : 
            ```shell
            $ ./runner.sh g
            ```

    * Inside docker container (only CLI version) :
        * Configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/server.yaml) file (set server host & port)
        * Build and run docker : 
            ```shell
            $ ./runner.sh host port
            ```
            ```shell
            $ ./runner.sh 0.0.0.0 6000
            ```

# Tests 🧪

The entire [server.server.Server](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/src/server/server.py) unit tests include within tests directory

### Run instructions :
* Install requirements:
    ```shell
    $ sudo pip3 install -r requirements.txt
    ```
* Run tests using [runner.sh](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/server/runner.sh)
    ```shell
    $ ./runner.sh t
    ```

<br>

# Copyright ©

👤 **Hadi Zaki AlQattan**

* Github: [@HadiZakiAlQattan](https://github.com/HadiZakiAlQattan)
* Email: [alqattanhadizaki@gmail.com]()

📝 **License**

Copyright © 2020 [Hadi Zaki AlQattan](https://github.com/HadiZakiAlQattan).<br />
This project is [MIT](https://github.com/HadiZakiAlQattan/sudoku/blob/master/LICENSE) licensed.

***
Give a ⭐️ if this project helped you!
