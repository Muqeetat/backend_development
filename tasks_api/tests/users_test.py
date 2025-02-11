import requests

# ====================================================================
# Adding a new user
# ====================================================================
# Send a POST request to add a new user with username 'Muqeetat' and password 'password'.
# Expectation: Successfully added the new user. Return the details of the user

# print("Adding a new User:")
# response = requests.post("http://127.0.0.1:8000/users",  
#     json={
#         "username": "Muqeetat",
#         "password": "password",
#     },
# )
# print(response.json())

# ====================================================================
# Fetching a user by ID
# ====================================================================
# Send a GET request to fetch the user with ID 2.
# Expectation: Return the details of the user with ID 2.

print("Fetching a task using ID:")
print(requests.get("http://127.0.0.1:8000/users/9").json())
print()
