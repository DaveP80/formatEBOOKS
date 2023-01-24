import fitz
import re
from re import search
from pathlib import Path
doc = fitz.open('./Konrath.pdf')
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
#print table of contents
#print(toc)
print(headerlist)
print(pagelist)
print(notpagelist)

with Path('newdocument.text').open(mode='w') as output_file_3:
    
    for i, page in enumerate(doc):
        if i in range(pagelist[0], pagelist[-1:][0]):
            content = page.get_text()
            output_file_3.write(content)      
        else:
            if i in range(pagelist[-1:][0]+1, notpagelist[-1:][0]):
                content = page.get_text()
                count = 0
                for s in range(len(substring)):
                    if not re.search(substring[s], content[0:25].lower()):
                        count += 1
                if count==len(substring):
                    output_file_3.write(content)

            if i>notpagelist[-1:][0]:
                if i>pagelist[-1:][0]:
                        content = page.get_text()
                        count = 0
                        if i in notpagelist:
                            quit()
                        else:
                            count = 0
                            for s in range(len(substring)):
                                count += 1
                                if not re.search(substring[s], content[0:25].lower()):
                                    count += 1
                            if count==len(substring):
                                output_file_3.write(content)

        
        # elif i in range(pagelist[0], pagelist[0]+1):
        #     content = page.get_text()
        #     count = 0
        #     for s in range(len(substring)):
        #         if not re.search(substring[s], content[0:25].lower()):
        #             count += 1

        #     if count==len(substring):
        #         output_file_3.write(content)