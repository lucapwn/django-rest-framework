import json
import requests

class API:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_token(self):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "username": self.username,
            "password": self.password
        }

        response = requests.post("http://127.0.0.1:8000/token/", headers=headers, data=json.dumps(payload))
        return response.text

    def get_users(self):
        token = json.loads(self.get_token())["access"]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        response = requests.get("http://127.0.0.1:8000/users/?format=json", headers=headers)
        return response.text

    def insert_user(self, name, document, email, telephone, birth_date, street, district, city, state, comments):
        token = json.loads(self.get_token())["access"]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        payload = {
            "name": name,
            "document": document,
            "email": email,
            "telephone": telephone,
            "birth_date": birth_date,
            "street": street,
            "district": district,
            "city": city,
            "state": state,
            "comments": comments
        }

        response = requests.post("http://127.0.0.1:8000/users/?format=json", headers=headers, data=json.dumps(payload))
        return response.text

    def update_user(self, id, name, document, email, telephone, birth_date, street, district, city, state, comments):
        token = json.loads(self.get_token())["access"]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        payload = {
            "name": name,
            "document": document,
            "email": email,
            "telephone": telephone,
            "birth_date": birth_date,
            "street": street,
            "district": district,
            "city": city,
            "state": state,
            "comments": comments
        }

        response = requests.put(f"http://127.0.0.1:8000/users/{id}/?format=json", headers=headers, data=json.dumps(payload))
        return response.text

    def delete_user(self, id):
        token = json.loads(self.get_token())["access"]

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }

        response = requests.delete(f"http://127.0.0.1:8000/users/{id}/?format=json", headers=headers)
        return response.text

def main():
    # Consider the user "admin" and password "admin" in the Django admin panel.
    # http://127.0.0.1:8000/admin/

    api = API(username="admin", password="admin")

    api.insert_user(name="Ana Santos", document="10293847561", email="ana@example.com", telephone="11987654321", birth_date="2000-01-01", street="Oscar Freire", district="Centro", city="São Paulo", state="SP", comments="No comments")
    api.insert_user(name="Lucas Araújo", document="29384756102", email="lucas@example.com", telephone="11987654321", birth_date="2000-01-02", street="Oscar Freire", district="Centro", city="São Paulo", state="SP", comments="No comments")
    api.update_user(id=1, name="Ana Carolina", document="10293847561", email="ana@example.com", telephone="11987654321", birth_date="2000-01-01", street="Oscar Freire", district="Centro", city="São Paulo", state="SP", comments="No comments")
    api.delete_user(id=2)

    print(api.get_users())

if __name__ == "__main__":
    main()
