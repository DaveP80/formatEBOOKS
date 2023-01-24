import fitz
import re
from re import search
#print(fitz.__doc__)
#doc = fitz.open('./Konrath.pdf')
doc = fitz.open('./SEHS.pdf')
toc = doc.get_toc()
#print(toc)
import os
import collections
#list of 2 nums, begin page and end page
pagelist = []
#list of page headers
headerlist = []
#print(toc)

substring = ['half title','title','title page','about the author','copyright','contents','author','introduction',
'references','glossary','index','notes','key terms','conclusions','appendix','appendix:','foreword','biography','preface',
'acknowledgments','afterword','postscript','prologue','bibliography']
for i, t in enumerate(toc[:len(toc)-2]):
    count = 0
    for s in range(len(substring)):
        if not re.search(substring[s], t[1].lower()):
            count += 1
    if not pagelist:
        if count==len(substring):
            pagelist.append(t[2]-2)
    else:
        if count==len(substring):
            pagelist.append(t[2])

for i, t in enumerate(toc[:len(toc)-2]):
    count = 0
    for s in range(len(substring)):
        if not re.search(substring[s], t[1].lower()):
            count += 1

    if count==len(substring):
        headerlist.append(t[1])
        
# for i, t in enumerate(toc[:len(toc)-2]):
#     if t[1].lower() not in substring:
#         headerlist.append(t[1])
#pagelist.append(doc.page_count)

print(headerlist)
print(pagelist)

for i, page in enumerate(doc):
    if i in range(pagelist[0], pagelist[-1:][0]+2):
        content = page.get_text()
        if i>pagelist[-1:][0]:
            count = 0
            for s in range(len(substring)):
                if not re.search(substring[s], content[0:25].lower()):
                    count += 1

            if count==len(substring):
                print(content)
        else:
            print(content)