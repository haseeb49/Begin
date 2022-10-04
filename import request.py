import webbrowser
import requests
url = 'https://jsonplaceholder.typicode.com/todos/'
#webbrowser.open(url)
data=requests.get(url)
print(data.json())
jjj