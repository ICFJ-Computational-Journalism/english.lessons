import requests
from bs4 import BeautifulSoup
import time

# Generate a timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S", time.localtime())

# URL of the CNN website section you want to scrape
url = 'https://www.cnn.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the elements containing the desired data
    data_elements = soup.find_all('span', {'data-editable': 'headline'})

    # Process the data elements
    scraped_data = []
    for element in data_elements:
        # Extract the specific information you need from each element
        data = element.text.strip()
        # Append the extracted data to the list
        scraped_data.append(data)

    # Save the scraped data to a timestamped file
    filename = f"data_{timestamp}.txt"
    with open(filename, 'w') as file:
        for data in scraped_data:
            file.write(data + '\n')

    # Optionally, you can print the scraped data
    for data in scraped_data:
        print(data)

else:
    print(f"Error: Failed to retrieve data from {url}. Status code: {response.status_code}")
