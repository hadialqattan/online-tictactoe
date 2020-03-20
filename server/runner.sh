set -e 

# run cli undockerized server
if [[ $1 == "c" ]]; then
    cd src && python main.py 0

# run gui undockerized server
elif [[ $1 == "g" ]]; then 
    cd src && python3 main.py

# dockerize the server and run it
elif [[ $# == 2 ]]; then 
    docker build -t online-ttt .
    echo "online-ttt image has been built successfully"
    docker run --rm -d --name online-ttt -h $1 -p $2 online-ttt
    echo "online-ttt is running..."
    echo ""
    echo "Stop command: ./runner.sh s"

# stop dockerized server
elif [[ $1 == "s" ]]; then 
    docker stop online-ttt 
    echo "online-ttt has been stopped!"

# start server tests using pytest (out side docker)
elif [[ $1 == "t" ]]; then 
    pytest -v tests/test_server.py

# show error statment
else
    echo "Invalid args, please take a look at server README.md file"
fi
