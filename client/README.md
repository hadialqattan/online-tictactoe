# Online-TicTacToe ([Client](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client))

> Online-tictactoe client is a client-side part of online-tictactoe game using python pygame lib aim to make a wonderful GUI for tictactoe game with simple network using socket and pickle lib.

# Usage 🗝

There are two ways to use this project :

* Using exe version without any requirements :
    * Download entire exe dir
    * Configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/exe/server.yaml) file (set server host & port)
    * Run exe/main.exe
    * Start playing ! [DEMO](#Demo)

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
    * Start playing [DEMO](#Demo)
    
        ![ttt-interface](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/init.jpg?raw=true)

# Demo  🧮
> You can play with any connected enemy or play with AI.

# Play Online (online)

## Start the server to start playing
* configure [server.yaml](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/server.yaml) file for client & server (2 files).
* start the server.
    
    ![start-the-server](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/start_server.gif?raw=true)

## Start playing with stable connection!
* choose empty square using (mouse/keyboard).
* hit enter to set a value.
* wherever you play, your enemy will see the result immediately.
    
    ![state-share](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/state_share.gif?raw=true)

## Winning / Losing cases
* the game will reseted.
* you symbol will changed.

    ![win-lose-cases](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/end_edge.gif?raw=true)

# Play With AI (offline & online)

## Change from online mode to AI mode
* press 'Play With AI' button.
* game will reseted and connection wont recv any data. 
* there are four AI engine level :
    * the level will automatically increased when you win.
    * maximum level is 4.
    * after each game you'll get a new playing symbol.
    
        ![change-to-ai-mode](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/setaimode.gif?raw=true)

## Set value and get AI response
* choose empty square using (mouse/keyboard). 
* hit enter to set a value. 
* you'll get AI response.
    
    ![ai-res](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/ai_res.gif?raw=true)

## Winning case
* AI engine level will increased.
* the game will reseted.
* your symbol will changed.
    
    ![win](https://github.com/HadiZakiAlQattan/online-tictactoe/blob/master/client/docs/win.gif?raw=true)

## Losing case 
* AI engine level wont increased. 
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
