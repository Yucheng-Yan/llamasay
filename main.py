import ast, subprocess, sys, os, ollama
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model(token):
	"""Load model and tokenizer"""
	tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B", token=token)
	model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-3B", token=token)
 
def token_getter():
	"""Check if the token is in the record"""
	file_exist = os.path.isfile("credentials.txt")
	if file_exist:
		f = open("credentials.txt", "r")
		token = (f.readline())
	else:
		f = open("credentials.txt", "x")
		token = input("Please enter your token: ")
		f.write(token)	
	return token

def validate_command(command):
	"""verify if a command is valid"""
	try:
		result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		return result
	except subprocess.CalledProcessError:
		return False

def suggest_commands(user_input):
	"""generate suggestions for a user input"""
	result_list = []
	while True:
		output = []
		prompt = f"There is a typo in the shell command '{user_input}', what command do you think the user intended to use? Only return a list of the top 5 possibilities. Return only the list without any additional text."
		
		response = ollama.chat(model='llama3:latest', messages=[
		{
			'role': 'user',
			'content': prompt,
		},
		])
		output = ast.literal_eval(response['message']['content'])
		
		for item in output:
			if item in common:
				result_list.append(item)
				return result_list

		return "Sorry, I can not find your intended command."

if __name__ == "__main__":
	common = [
		"ls", "cd", "pwd", "mkdir", "rmdir", "rm", "cp", "mv", "touch", "cat", "more",
    		"less", "head", "tail", "find", "chmod", "chown", "ln", "df", "du", "nano", 
       		"vi", "vim", "echo", "grep", "sed", 	"awk", "sort", "uniq", "cut", "wc", 
          	"tr", "tar", "zip", "unzip", "gzip", "gunzip", "ssh", "scp", "curl", "wget", 
            	"ping", "top", "htop", "ps", "kill", "killall", "bg", "fg", "jobs", "nohup", 
             	"disown", "alias", "unalias", "history", "clear", "man", "which", "who", 
              	"whoami", "uptime", "uname", "env", "export", "source", "sudo", "apt", "yum", 
               	"dnf", "pacman", "brew", "systemctl", "service", "crontab", "at", "mount", 
                "umount", "free", "lsof", "netstat", "ip", "ifconfig", "iptables", 
                "traceroute", "dig", "nslookup", "hostname", "date", "cal", "bc", "printf", 
                "read",	"seq", "sleep", "wait", "expr", "test", "true", "false", "xargs", 
                "tee", "basename", "dirname", "diff", "patch", "ssh-keygen", "ssh-copy-id", 
                "rsync", "ftp", "smbclient", "smbmount", "screen", "tmux", "chattr", "lsattr", 
                "md5sum", "sha256sum", "cmp", "split", "cksum"
    		]

	print("Welcome to llamasay! Type a command to run or type 'exit' to quit.")
	token = token_getter()
	load_model(token)

	while True:
		user_input = input("% ")

		if user_input == "exit":
			sys.exit(0)
		
		result = validate_command(user_input)
		if result:
			print(result.stdout.decode().rstrip())
		else:
			print("Invalid command. Generating suggestions...")
			suggestions = suggest_commands(user_input)
			if isinstance(suggestions, str):
				print(suggestions)
			else:
				print("Did you mean:")
				print(suggestions)

