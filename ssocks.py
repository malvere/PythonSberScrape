import base64

import requests

from reg_decode import reg_decode

# URL of the file to fetch
url = 'https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the content of the response
        content = response.content

        # Decode the content as base64
        decoded_content = base64.b64decode(content)

        # Decode the decoded content as UTF-8 text
        text_content = decoded_content.decode('utf-8')

        # Split the text into lines
        lines = text_content.split('\n')

        # Filter lines that start with "ss://"
        ss_lines = [line for line in lines if line.startswith("ss://")]

        # Print the filtered lines
        for ss_line in ss_lines:
            reg_decode(ss_line)
            print(ss_line)
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
