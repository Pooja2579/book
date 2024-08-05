import requests

def fetch_books_from_google(query):
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key=AIzaSyAybHwd0hM2q5sKq1Nbqt2ijhE-18ILrRQ'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None
