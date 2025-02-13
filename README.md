# Backend Development Task

## Section One: String Compression & First Non-Repeating Character

### 1. String Compression
**Function**: `compress(string: str) -> str`  
Compresses a string by counting consecutive characters. If the compressed string is longer or equal to the original, returns the original string.

**Test Cases**:
```python
assert compress('bbcceeee') == 'b2c2e4'
assert compress('aaabbbcccaaa') == 'a3b3c3a3'
assert compress('a') == 'a'
```

### 2. First Non-Repeating Character
**Function**: `first_non_repeating(string: str) -> str`  
Finds the first non-repeating character. Returns `-1` if all characters repeat.

**Example**:
- Input: `"swiss"`
- Output: `-1`

---

## Section Two: Task Management API

### Features:
- Task categorization (e.g., "Work", "Personal")
- Pagination for tasks

### Setup:
1. Clone the repository.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run the app:  
   `uvicorn app.main:app --reload`

### API Docs:
Access via:  
`http://127.0.0.1:8000/docs`

