# import requests


# print("Root path:")
# print(requests.get("http://127.0.0.1:8000/").json())
# print()



# print("Fetching all tasks:")
# print(requests.get("http://127.0.0.1:8000/tasks").json())
# print()



# print("Fetching a task using ID:")
# print(requests.get("http://127.0.0.1:8000/tasks/42").json())
# print()


# print("Adding a Task:")
# response = requests.post(
#     "http://127.0.0.1:8000/tasks",  
#     json={
#         "title": "Washing Rice",
#         "description": "Cooking Rice",
#         "category": "Chores",
#         "status": "in-progress",
#         "due_date": "2025-02-20 12:00:00"
#     },
# )
# print(response.json())



# print("Updating an item:")
# response = requests.put(
#     "http://127.0.0.1:8000/tasks/42",
#     json={
#         "title": "Learning Japanese",
#         "description": "Language"
# 		}
# )
# print(response.json())
# print()

 

# print("Deleting an item:")
# response = requests.delete("http://127.0.0.1:8000/tasks/42")
# if response.status_code == 204:  # No Content
#     print("Task deleted successfully.")
# else:
#     print(response.json())


# ====================================================================
# Adding a new user
# ====================================================================
# Send a POST request to add a new user with username 'Muqeetat' and password 'password'.
# Expectation: Successfully added the new user. Return the details of the user

# print("Adding a new User:")
# response = requests.post("http://127.0.0.1:8000/users",  
#     json={
#         "name": "pass",
#         "password": "pass",
#     },
# )
# print(response.json())

# ====================================================================
# Fetching a user by ID
# ====================================================================
# Send a GET request to fetch the user with ID 2.
# Expectation: Return the details of the user with ID 2.

# print("Authenticate User with wrong password:")
# response = requests.post(
#     "http://127.0.0.1:8000/login",  
#     data={  # Use data for form data
#         "username": "user",
#         "password": "u",
#     }
# )

# # Check the status code first
# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Error:", response.text)

# ====================================================================
# Fetching a user by ID
# ====================================================================
# Send a GET request to fetch the user with ID 2.
# Expectation: Return the details of the user with ID 2.

# print("Authenticate User with right password:")
# login_data = {"username": "pass", "password": "pass"}

# response = requests.post("http://127.0.0.1:8000/login", data=login_data)

# if response.status_code == 200:
#     access_token = response.json().get("access_token")
#     print("Token:", access_token)
# else:
#     print("Login Error:", response.text)

# ====================================================================
# Fetching a user by ID
# ====================================================================
# Send a GET request to fetch the user with ID 2.
# Expectation: Return the details of the user with ID 2.


# login_url = "http://127.0.0.1:8000/login"
# credentials = {"username": "user", "password": "user"}

# response = requests.post(login_url, data=credentials)

# if response.status_code == 200:
#     access_token = response.json()["access_token"]
#     print("New Token:", access_token)
# else:
#     print("Login Failed:", response.text)