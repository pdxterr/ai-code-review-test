def vulnerable_login(username, password):
    # Security issue: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Quality issue: No input validation
    if len(username) == 0:
        return None
        
    # Architecture issue: Direct database connection in business logic
    import sqlite3
    conn = sqlite3.connect("users.db")
    result = conn.execute(query).fetchone()
    
    return result

def calculate_score(data):
    # Quality issue: No error handling
    total = data["points"] + data["bonus"]  
    
    # Architecture issue: Magic numbers
    if total > 1000:
        total = 1000
        
    return total * 0.75  # More magic numbers
