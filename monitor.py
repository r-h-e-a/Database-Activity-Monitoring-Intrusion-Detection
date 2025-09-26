import sqlparse

# Example SQL queries
queries = [
    "SELECT * FROM users;",
    "DROP TABLE users;",
    "DELETE FROM orders WHERE id=5;",
    "SELECT name FROM customers WHERE id=1;"
]

def log_query(query):
    print(f"[LOG] Executing query: {query}")

def detect_suspicious(query):
    keywords = ["DROP", "DELETE", "TRUNCATE"]
    return any(word in query.upper() for word in keywords)

for q in queries:
    log_query(q)
    if detect_suspicious(q):
        print(f"[ALERT] Suspicious query detected: {q}")
