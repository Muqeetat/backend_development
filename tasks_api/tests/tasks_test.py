import requests

# ====================================================================
# Checking 'gold.dim_customers'
# ====================================================================
# Check for Uniqueness of Customer Key in gold.dim_customers
# Expectation: No results

# print("Root path:")
# print(requests.get("http://127.0.0.1:8000/").json())
# print()

# ====================================================================
# Checking 'gold.dim_customers'
# ====================================================================
# Check for Uniqueness of Customer Key in gold.dim_customers
# Expectation: No results 

# print("Fetching all tasks:")
# print(requests.get("http://127.0.0.1:8000/tasks").json())
# print()

# ====================================================================
# Checking 'gold.dim_customers'
# ====================================================================
# Check for Uniqueness of Customer Key in gold.dim_customers
# Expectation: No results 

# print("Fetching a task using ID:")
# print(requests.get("http://127.0.0.1:8000/tasks/42").json())
# print()

# ====================================================================
# Checking 'gold.dim_customers'
# ====================================================================
# Check for Uniqueness of Customer Key in gold.dim_customers
# Expectation: No results 

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

# ====================================================================
# Checking 'gold.dim_customers'
# ====================================================================
# Check for Uniqueness of Customer Key in gold.dim_customers
# Expectation: No results 


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

# ====================================================================
# Checking 'gold.dim_customers'
# ====================================================================
# Check for Uniqueness of Customer Key in gold.dim_customers
# Expectation: No results 

# print("Deleting an item:")
# response = requests.delete("http://127.0.0.1:8000/tasks/42")
# if response.status_code == 204:  # No Content
#     print("Task deleted successfully.")
# else:
#     print(response.json())


