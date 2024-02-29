import json
import subprocess

def handle_json_data(post_data):
    try:
        json_data = json.loads(post_data.decode('utf-8'))
        # Handle the JSON data as needed
        print("Received JSON data:", json_data)

        if 'Buy BTC' in json_data and json_data['Buy BTC'] == 100:
            # Execute a Python script or command when the specific message is received
            subprocess.run(['python', 'Buy.py'])

            # Respond with a success message
            response_data = {'message': 'Buy BTC command executed successfully'}

        elif 'Sell BTC' in json_data and json_data['Sell BTC'] == 100:
            # Execute a different Python script or command when the specific message is received
            subprocess.run(['python', 'Sell.py'])

            # Respond with a success message
            response_data = {'message': 'Sell BTC command executed successfully'}
        else:
            # Respond with a default success message for other messages
            response_data = {'message': 'JSON data received successfully'}

        return 200, response_data

    except json.JSONDecodeError:
        return 400, {'error': 'Invalid JSON data'}

# This part is not intended for running a server on Render.
# Render will automatically serve static files in the public directory.
# Please deploy this as a static site on Render.

if __name__ == '__main__':
    print("This script is not intended for running a server on Render.")
    print("Render will automatically serve static files in the public directory.")
    print("Please deploy this as a static site on Render.")
