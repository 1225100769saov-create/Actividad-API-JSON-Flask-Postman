import requests

BASE = "https://jsonplaceholder.typicode.com"

# POST
nuevo = {"title": "Prueba de red", "body": "Contenido de ejemplo", "userId": 1}
r = requests.post(f"{BASE}/posts", json=nuevo, timeout=10)
print("POST:", r.status_code, r.json())

# PUT
r = requests.put(f"{BASE}/posts/1", json={**nuevo, "id": 1}, timeout=10)
print("PUT:", r.status_code, r.json())

# DELETE
r = requests.delete(f"{BASE}/posts/1", timeout=10)
print("DELETE:", r.status_code)

print("Samuel Antonio Olvera Villegas")