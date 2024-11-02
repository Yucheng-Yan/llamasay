# llamasay

Llamasay is a Bash-based software that can correct typos in Bash commands, powered by the [Llama 3 model](https://ai.meta.com/blog/meta-llama-3/).

## Installation

``````bash
git clone git@github.com:Yucheng-Yan/llamasay.git
cd llamasay
python3 main.py
``````

## Examples

```bash
(venv) lcthw@Yuchengs-MacBook-Air llamasay % py main.py     
Welcome to llamasay! Type a command to run or type 'exit' to quit.
# Bash commands will be run as usual
% pwd
/Users/lcthw/llamasay # The path of working directory is printed
# If the input is invalid, the program will call Llama3 API and to guess the intended command.
% pwf
Invalid command. Generating suggestions...
Did you mean:
['pwd'] # Ouput the most possible command.
# Another example
% who
lcthw            console      Oct 27 05:56 
lcthw            ttys000      Nov  1 22:25 
% whp
Invalid command. Generating suggestions...
Did you mean:
['who']
# When the program is unable to find any command similar to the one the user input, it prints out a message to inform the user.
% xxx
Invalid command. Generating suggestions...
Sorry, I can not find your intended command.
% exit
```

