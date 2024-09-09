import requests
import threading

def send_requests():
    while True:
        try:
            response = requests.get("http://127.0.0.1:5000/")
            print(f"Response Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

# Number of threads (simulates multiple users attacking at once)
threads = []

for i in range(100):  # Adjust the number for more intensity
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
