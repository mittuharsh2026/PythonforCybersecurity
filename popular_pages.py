f = open("access.log", "r")

pages = {}

while True:
    line = f.readline()

    if not line:
        break

    parts = line.split()

    if len(parts) > 6:
        page = parts[6]

        if page in pages:
            pages[page] += 1
        else:
            pages[page] = 1

f.close()

print("Most Popular Pages:")

for page in sorted(pages, key=pages.get, reverse=True):
    print(page, pages[page])
