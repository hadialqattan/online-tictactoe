# Online-TicTacToe ([Server](https://github.com/hadialqattan/online-tictactoe/blob/master/server))

> Online-tictactoe server is a server-side part of online-tictactoe game using python socket lib and pickle lib aim to make a stable connection between two threaded tictactoe players and send/recv data from/to players as objects using pickle lib.

# Usage 🗝

There are two ways to use the server :

* Using exe version without any requirements :
    * Download entire exe dir
    * Configure [server.yaml](https://github.com/hadialqattan/online-tictactoe/blob/master/server/exe/server.yaml) file (set server host & port)
    * Run exe/[main.exe](https://github.com/hadialqattan/online-tictactoe/blob/master/server/exe/main.exe)
    * Press start button
   
        ![server gui jpg](https://github.com/hadialqattan/online-tictactoe/blob/master/server/docs/server_gui.jpg?raw=true)

* Using [runner.sh](https://github.com/hadialqattan/online-tictactoe/blob/master/server/runner.sh) and there are three ways:  
    
    * Inside your machine (both CLI & GUI) :
        * Install requirements: 
            ```shell
            $ sudo pip3 install -r requirements.txt
            ```
        * Configure [server.yaml](https://github.com/hadialqattan/online-tictactoe/blob/master/server/server.yaml) file (set server host & port)
        * CLI : 
            ```shell 
            $ ./runner.sh c
            ```
        * GUI : 
            ```shell
            $ ./runner.sh g
            ```

    * Inside docker container (only CLI version) :
        * Configure [server.yaml](https://github.com/hadialqattan/online-tictactoe/blob/master/server/server.yaml) file (set server host & port)
        * Build and run docker : 
            ```shell
            $ ./runner.sh host port
            ```
            ```shell
            $ ./runner.sh 0.0.0.0 6000
            ```

# Tests 🧪

The entire [server.server.Server](https://github.com/hadialqattan/online-tictactoe/blob/master/server/src/server/server.py) unit tests include within tests directory

### Run instructions :
* Install requirements:
    ```shell
    $ sudo pip3 install -r requirements.txt
    ```
* Run tests using [runner.sh](https://github.com/hadialqattan/online-tictactoe/blob/master/server/runner.sh)
    ```shell
    $ ./runner.sh t
    ```