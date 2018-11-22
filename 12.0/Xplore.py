import json

N = int(input())
authors_citations = {}
for i in range(N):
    line = input()
    json_object = json.loads(line)
    authors = json_object["authors"]["authors"]
    citations = json_object["citing_paper_count"]
    for obj in authors:
        author_name = obj["full_name"]
        if author_name in authors_citations.keys():
            ac = authors_citations[author_name]
            ac.append(citations)
            authors_citations[author_name] = ac
        else:
            authors_citations[author_name] = [citations]

A = authors_citations.keys()
C = []
for a in A:
    a_citations = authors_citations[a]
    a_citations.sort()
    a_citations.reverse()
    c = 0
    for j in range(len(a_citations)):
        if a_citations[j] >= (j+1):
            c = j+1
        else:
            break
    C.append((a, c))
C = sorted(C, key=lambda x: (-x[1], x[0]))

for c in C:
    print(c[0], end=" ")
    print(c[1])