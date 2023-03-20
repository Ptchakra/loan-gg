from os import stat
from rich import print


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "nội thất văn phòng"
total = []
for j in search(query, tld="co.in", num=300, start=200, pause=2):
    domain = j.split("//")[0] + "//" + j.split("//")[1].split("/")[0]
    print(domain)
    total.append(domain)
total = sorted(total)
total = list(set(total))
print(len(total))
string = "\n".join(total)
with open("data3.txt", "w") as f:
    f.write(string)
