# llamasay

Llamasay is a Bash-based program that can guess the command the user intended to input (by calling a large language model) when the user enters invalid Bash commands.

## Prerequisite
To use llamasay, you will need to set up [ollama](https://ollama.com/) and get at least one model you want to use.

## Installation

``````bash
git clone git@github.com:Yucheng-Yan/llamasay.git
cd llamasay
python3 main.py
``````

## Set up
The first time you use llamasay, the program will prompt you to enter your [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).

After you enter it for the first time, you will not need to enter it again in the future.


## Examples
After running `python3 main.py`, you should see the message below:
```bash
(venv) lcthw@Yuchengs-MacBook-Air llamasay % python3 main.py     
Welcome to llamasay! Type a command to run or type 'exit' to quit.
```

Bash commands will be run as usual
```bash
% pwd
/Users/lcthw/llamasay # The path of working directory is printed
```
If the input is invalid, the program will call Llama3 (by default) API to guess the intended command.
```bash
% pwf
Invalid command. Generating suggestions...
Did you mean:
['pwd'] # Ouput the most possible command.
```
Another example
```bash
% who
lcthw            console      Oct 27 05:56 
lcthw            ttys000      Nov  1 22:25 
% whp
Invalid command. Generating suggestions...
Did you mean:
['who']
```
When the program is unable to find any command similar to the one the user input, it prints out a message to inform the user.
```bash
% xxx
Invalid command. Generating suggestions...
Sorry, I can not find your intended command.
```
To exit llamasay, run
```bash
% exit
```

