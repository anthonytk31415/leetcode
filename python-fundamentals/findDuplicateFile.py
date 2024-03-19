from collections import defaultdict

def findDuplicate(paths):
    def extractStuff(s):
        idx = s.find("(")
        return s[:idx], s[(idx+1):-1]

    dupeHolder = defaultdict(list) # content : [path1, path2, ...]

    for path in paths: 
        files = path.split(" ")
        curPath = files[0]
        for i in range(1, len(files)):
            curFileName, curFileContent = extractStuff(files[i])
            dupeHolder[curFileContent].append(curPath + "/" + curFileName)

    return [dupeHolder[x] for x in dupeHolder if len(dupeHolder[x]) > 1]

a = "3.txt(abcd)"



print(extractStuff(a))


paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

print(findDuplicate(paths))