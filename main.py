import subprocess
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM

user_token = input("Please enter your token: ")

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B", token=user_token)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-3B", token=user_token)

def validate_command(command):
	"""verify if a command is valid"""
	try:
		subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		return True
	except subprocess.CalledProcessError:
		return False

def suggest_commands(user_input):
	"""generate suggestions for a user input"""
	input_ids = tokenizer.encode(f"There is a typo in the shell command '{user_input}', what command do you think the user intended to use? Only return a list of the top 3 possibilities including a brief explanation for each. Return only the list without any additional text.", return_tensors='pt')
	output = model.generate(input_ids, max_new_tokens=50, temperature=0.7, top_p=0.9)
	suggestions = tokenizer.decode(output[0], skip_special_tokens=True)
	return suggestions

if __name__ == "__main__":
	print("Welcome to llamasay! Type a command to run or type 'exit' to quit.")
 
	while True:
		user_input = input("% ")
  
		if user_input == "exit":
			sys.exit(0)

		if validate_command(user_input):
			subprocess.run(user_input, shell=True)
		else:
			print("Invalid command. Generating suggestions...")
			suggestions = suggest_commands(user_input)
			print("Did you mean:")
			print(suggestions)

