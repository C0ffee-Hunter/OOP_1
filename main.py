import requests

print("Введите статью, которую вы ищите в Википедии:")
user_request = str(input())
user_request = user_request.replace(' ', '+')

url_json = "https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch=" + user_request

r = requests.get(url_json)

i = 0
while i != 5:
    print("Название страницы: " + r.json()["query"]['search'][i]['title'])
    title = r.json()["query"]['search'][i]['title']

    print("ID страницы: " + str(r.json()["query"]['search'][i]['pageid']))
    page_id = r.json()["query"]['search'][i]['pageid']

    url_page = "https://ru.wikipedia.org/w/index.php?curid=" + str(page_id)
    print("Ссылка на статью:")
    print(url_page + "\n")
    i = i + 1
