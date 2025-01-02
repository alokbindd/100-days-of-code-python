import multiprocessing
import requests
import concurrent.futures

def DownloadFile(url,name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"D:/Python-lang/98-Day-98-MultiProcessing-in-Python/files/file{name}.jpg","wb").write(response.content)
    print(f"Downloaded {name}")

url = "https://picsum.photos/2000/3000"

if __name__ == '__main__':
#     pros = []
#     for i in range(50):
#         # DownloadFile(url,i)
#         p = multiprocessing.Process(target=DownloadFile,args=[url,i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(50)]
        l2 = [i for i in range(50)]
        result = executor.map(DownloadFile,l1,l2)
        for r in result:
            print(r)

