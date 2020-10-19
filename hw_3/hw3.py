import json
import csv


def get_users():
    with open("json/users.json") as f:
        result = json.load(f)
    return result


def get_books():
    result = []
    with open('csv/books.csv') as f:
        reader = csv.reader(f)

        # Извлекаем заголовок
        header = next(reader)

        # Итерируемся по данным делая из них словари
        for row in reader:
            item = dict(zip(header, row))
            result.append(item)

    return result


users = get_users()
books = get_books()[:5]

for user, book in zip(users, books):
    user['books'] = [book]

for user in users:
    if 'books' not in user:
        user['books'] = []

with open('json/example.json', 'w') as f:
    json.dump(users, f, indent=2)
