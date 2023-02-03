file_name = '/Users/shanliangyao/workspace/study/mypaper/Radar-Camera-Fusion-IEEE/Fusion.bib'

content = open(file_name).read()

with open(file_name, 'r') as r:
    lines=r.readlines()

with open(file_name, 'w') as w:
    for l in lines:
       	if not (l.startswith('note') or l.startswith('abstract') or l.startswith('local-url')):
            w.write(l)
        else:
            print(l)

print("Done!")