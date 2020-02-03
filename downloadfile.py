import requests
import math
import tqdm

url = input("Enter Link : ")

chunk_size = 256
r = requests.get(url, stream=True)

n = math.ceil(int(r.headers['Content-length']) / chunk_size)

with open("large.pdf", "wb") as file:
    for chunk in tqdm.tqdm(r.iter_content(chunk_size=chunk_size), total=n):
        file.write(chunk)
