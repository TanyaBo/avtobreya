import csv
import re

header = ('prevword', 'nextword', 'prevtag', 'nexttag', 'class')
rows = []
punct = '”“".,«»\\/*!:;—()\'-%`.?'

with open('output.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        words = line.split()
        for i in words:
            try:
                word = re.search('{(.*?)=', i)
                word = word.group(1)
            except AttributeError:
                continue
                if 'фигура' in word:
                    cl = i.split('_')[1]
                print(cl)
##                    prevword, prevtag = words[w - 1].split('/')
##                    if prevword in punct:
##                        prevword, prevtag = words[w - 2].split('/')
##                    nextword, nexttag = words[w + 1].split('/')
##                    if nextword in punct:
##                        try:
##                            nextword, nexttag = words[w + 2].split('/')
##                        except IndexError:
##                            pass
##                    rows.append((prevword.replace(',', '').replace('\'', ''), nextword.replace(',', '').replace('\'', ''), prevtag.replace('$', ''), nexttag.replace('$', ''), cl))
##            except ValueError:
##                continue
##
##
##with open('interest.csv', 'w', encoding='utf-8') as w:
##    out = csv.writer(w, delimiter=',')
##    out.writerow(header)
##    out.writerows(rows)
##                
