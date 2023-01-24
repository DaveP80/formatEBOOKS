import fitz
import re
from re import search
from pathlib import Path
doc = fitz.open('./EJ.pdf')
toc = doc.get_toc()
#list of nums, begin page and end page
pagelist = []
#list of page headers
headerlist = []

substring = ['half title','title','title page','about the author','copyright','contents','author','introduction',
'references','glossary','index','notes','key terms','conclusions','appendix','appendix:','foreword','biography',
'dedication','disclaimers','preface','safety notices','number of printings'
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
#print table of contents
print(toc)
print(pagelist)

with Path('newdocument.text').open(mode='w') as output_file_3:
    
    for i, page in enumerate(doc):
        if i in range(pagelist[1], pagelist[-1:][0]+2):
            content = page.get_text()
            if i>pagelist[-1:][0]:
                count = 0
                for s in range(len(substring)):
                    if not re.search(substring[s], content[0:25].lower()):
                        count += 1

                if count==len(substring):
                    output_file_3.write(content)
            else:
                output_file_3.write(content)
        
        elif i in range(pagelist[0], pagelist[0]+1):
            content = page.get_text()
            count = 0
            for s in range(len(substring)):
                if not re.search(substring[s], content[0:25].lower()):
                    count += 1

            if count==len(substring):
                output_file_3.write(content)