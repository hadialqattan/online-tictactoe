set -e 

# run GUI game
if [[ $1 == "g" ]]; then 
    cd src && python3 main.py

# run CLI all tests
elif [[ $1 == "t" ]]; then 
    echo ""
    pytest -v tests/test_network.py
    echo ""
    pytest -v tests/test_tictactoe.py
    echo ""
    pytest -v tests/test_ai.py
    echo ""

# run CLI network tests 
elif [[ $1 == "tn" ]]; then 
    pytest -v tests/test_network.py

# run CLI tictactoe tests 
elif [[ $1 == "tt" ]]; then 
    pytest -v tests/test_tictactoe.py

# run CLI ai tests 
elif [[ $1 == "ta" ]]; then 
    pytest -v tests/test_ai.py

# show error statment
else
    echo "Invalid args, please take a look at client README.md file"
fi
