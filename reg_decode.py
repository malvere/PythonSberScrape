import base64
import re
import urllib.parse

# Input line
line = 'ss://YWVzLTEyOC1jZmI6c2hhZG93c29ja3M=@156.146.38.163:443#%F0%9F%87%BA%F0%9F%87%B8US-156.146.38.163-0192'
def reg_decode(input_line: str):

# Define a regular expression pattern to match the components
    pattern = r'ss://([^@]+)@(\d+\.\d+\.\d+\.\d+):(\d+)#(%[^-]+)-(\d+)'

    # Use re.search to find the match
    match = re.search(pattern, input_line)

    if match:
        # Extract the matched components
        base64_string = match.group(1)
        ip_address = match.group(2)
        port = match.group(3)
        emoji_and_name = urllib.parse.unquote(match.group(4))
        additional_info = match.group(5)

        # Decode the base64 string
        decoded_bytes = base64.b64decode(base64_string)
        decoded_string = decoded_bytes.decode('utf-8')

        # Separate emoji and name
        emoji = emoji_and_name[:2]  # Assuming the emoji is always 2 characters
        name = emoji_and_name[2:]
        pwd = base64.urlsafe_b64decode(base64_string)
        pwd_text = pwd.decode('utf-8')
        print("Password String:", pwd_text)
        print("IP Address:", ip_address)
        print("Port:", port)
        print("Emoji:", emoji)
        print("Name:", name)
        print("Additional Info:", additional_info)
        print("-" * 20)
    else:
        print("No match found in the input line.")

reg_decode(line)