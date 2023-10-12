import requests
from bs4 import BeautifulSoup

def find_second_to_last_stats_pager_li(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all elements with the specified class
            li_elements = soup.find_all("li", class_="stats-pager__li")

            # Check if there are at least two elements
            if len(li_elements) >= 2:
                # Find the second-to-last element
                second_to_last_element = li_elements[-2]

                # Return the text content of the second-to-last element
                return second_to_last_element.text
            else:
                return 1
        else:
            return f"Failed to retrieve the web page. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Usage
url = "https://www.ncaa.com/stats/basketball-men/d2/current/individual/556"
result = find_second_to_last_stats_pager_li(url)
print("Result:")
print(result)
