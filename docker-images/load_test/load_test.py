import requests
from collections import defaultdict

url = "http://localhost/"
num_requests = 300
replica_counts = defaultdict(int)

for _ in range(num_requests):
    response = requests.get(url)
    replica_ip = response.cookies.get('replica_ip')
    replica_counts[replica_ip] += 1
    print(f"Replica IP: {replica_ip}, Cookies: {response.cookies}")

for replica, count in replica_counts.items():
    print(f"Replica {replica} received {count} connections")
