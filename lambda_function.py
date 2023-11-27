import json
import requests
import random

def lambda_handler(event, context):
    def generate_random_cat():
        url = 'https://cataas.com/api/cats?tags=cute'
        response = requests.get(url)
        data = json.loads(response.text)

        # Select a random cat image from the response
        random_cat = random.choice(data)

        # Access the image URL and other information
        image_url = f"https://cataas.com/cat/{random_cat['_id']}"
        mimetype = random_cat['mimetype']
        size = random_cat['size']
        tags = random_cat['tags']

        # Return the image URL or perform any desired actions
        return image_url

    # Example usage
    random_cat_image = generate_random_cat()

    # Generate an HTML response with the image URL
    html_response = f"""
    <html>
    <body>
        <h1>Random Cat Image</h1>
        <img src="{random_cat_image}" alt="Random Cat">
    </body>
    </html>
    """

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_response
    }

