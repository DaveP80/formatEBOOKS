import fitz
import re
from re import search
from pathlib import Path
doc = fitz.open('./EJ.pdf')
toc = doc.get_toc()
#list of nums, begin page and end page
pagelist = []
#bad page list
notpagelist = []
#list of page headers
headerlist = []

substring = ['half title','title','title page','about the author','copyright','contents','author','introduction',
'references','glossary','index','notes','key terms','conclusions','appendix','appendix:','foreword','biography',
'dedication','disclaimers','preface','safety notices','number of printings'
'acknowledgments','afterword','postscript','prologue','bibliography']

print(toc)

for i, t in enumerate(toc[:len(toc)-1]):
    count = 0
    for s in range(len(substring)):
        if not re.search(substring[s], t[1].lower()):
            count += 1
        if re.search(substring[s], t[1].lower()):
            notpagelist.append(t[2])
    if not pagelist:
        if count==len(substring):
            pagelist.append(t[2])
    else:
        if count==len(substring):
            pagelist.append(t[2])

for i, t in enumerate(toc[:len(toc)-1]):
    count = 0
    for s in range(len(substring)):
        if not re.search(substring[s], t[1].lower()):
            count += 1

    if count==len(substring):
        headerlist.append(t[1])

print(pagelist)

with Path('newdocument.text').open(mode='w') as output_file_3:
    count = 0
    check = False
    for i in range(len(notpagelist)):
        if notpagelist[i]<pagelist[-1:][0]:
            count += 1
    if count<len(notpagelist):
        check = True
    if count==len(notpagelist):
        innercount = 0
        checklist = pagelist[-10:]
        for r in range(len(checklist)):
            if notpagelist[-1:][0]<checklist[r]:
                innercount += 1
        if innercount==len(checklist):
            notpagelist= []

    if notpagelist:
        if not check:
            for i in range(len(notpagelist)):
                if notpagelist[i]<pagelist[-1:][0]:
                    if notpagelist[i]>pagelist[0]:
                        for j in range(len(pagelist)):
                            if pagelist[j]>notpagelist[i]:
                                #if we have a good not page list
                                pagelist.remove(pagelist[j])

    for p, page in enumerate(doc):
        if p in range(pagelist[0], pagelist[-1:][0]):
            content = page.get_text()
            output_file_3.write(content)      
        else:
            if notpagelist:
                if p in range(pagelist[-1:][0]+1, notpagelist[-1:][0]):
                    content = page.get_text()
                    count = 0
                    for z in range(len(notpagelist)):
                        if notpagelist[z]>pagelist[-1:][0]:
                            if p==notpagelist[z]:
                                quit()
                    for s in range(len(substring)):
                        if not re.search(substring[s], content[0:25].lower()):
                            count += 1
                    if count==len(substring):
                        output_file_3.write(content)

            if not notpagelist:
                if p in range(pagelist[-1:][0]+1, doc.page_count):
                    content = page.get_text()
                    count = 0
                    for s in range(len(substring)):
                        if not re.search(substring[s], content[0:25].lower()):
                            count += 1
                    if count>0:
                        quit()
                    if count==len(substring):
                        output_file_3.write(content)
