from collections import OrderedDict, defaultdict, deque
from math import inf


# wow what a beast.
# the main issue here is that when you BFS, you'll need to create a lot of paths. 

# We'll BFS to get the path tree. Then we'll DFS the parents to get the actual paths.
# we do this because if we were to maintain the path during BFS for each path, we create
# a shit ton of memory for paths that don't lead to the end.

# BFS: 
# so we'll BFS to find the shortest paths from the beginWord to the endWord. And on 
# the path, we'll just keep a tree of parents where a given node can have multiple parents. 
# In the BFS, at each breadth, we will keep a global visited and a level visited dictionary. 
# Using the level-visited, when we enqueue you for the first time, you get put in that level
# We will enqueue the next node once, but if you can arrive at "next node" if you traverse there
# from a node in the same level (hence multiple parents).
# We never revisit nodes in the global visited (because there will be a cycle and you'll get a larger path).

# DFS: 
# We'll traverse from the end to then beginning to keep memory tight and we'll get the parents from the 
# path parent tree that is returned from BFS.
# Finally we'll return the DFS result as the answer. 

# Time: O(n) as each node 
# space: O(N)

def findLadders(beginWord, endWord, wordList):

    def bfs(beginWord, endWord, wordList):
        # create the adjacency list
        graph = defaultdict(list)                   # "hit" --> key = 'h*t', val = 'hit; this is to search for next paths 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '.' + word[i+1:]
                graph[pattern].append(word)

        q = deque([beginWord])

        # create a globaly visited key;value = node: [node how you got there] (like a parents list)
        all_visited = defaultdict(list)
        found_end = False
        while q and not found_end:
            visited_this_level = defaultdict(list)
            for _ in range(len(q)):     # go through each depth so you can accommodate other nodes that reach the end in the same level
                curNode = q.popleft()
                if curNode == endWord:                      # terminal cond: is node == end?   
                    found_end == True                       # 
                else: 
                    for i in range(len(curNode)):
                        curNodePattern = curNode[:i] + '.' + curNode[i+1:]
                        for nextNode in graph[curNodePattern]:
                            if nextNode not in all_visited:
                                if nextNode not in visited_this_level:
                                    q.append(nextNode)        
                                visited_this_level[nextNode].append(curNode)
            all_visited.update(visited_this_level)
        return all_visited

    # traverse from end to begin; 
    # you'll recursively build the parent tree and then for each path in res, you'll append the endWord
    def dfs(beginWord, endWord, wordTree):
        if beginWord == endWord: 
            return [[beginWord]]
        if endWord not in wordTree:
            return []
        res = []
        parents = wordTree[endWord]
        for parent in parents:
            res += dfs(beginWord, parent, wordTree)
        for partialRes in res: 
            partialRes.append(endWord)
        return res


    wordTree = bfs(beginWord, endWord, wordList)
    res = dfs(beginWord, endWord, wordTree)
    return res






# # this is too slow because of the path.

# def findLadders(beginWord, endWord, wordList):
#     res = []
#     wordList = set(wordList)
#     wordList.add(beginWord)

#     if endWord not in wordList:
#         return res

#     # def countCompare(word1, word2):
#     #     errors = 0
#     #     for i in range(len(word1)):
#     #         if word1[i] != word2[i]: errors +=1
#     #         if errors > 1: 
#     #             return False 
#     #     return True

#     dist = {x: inf for x in wordList}
#     dist[beginWord] = 0

#     queue = deque()
#     queue.append([beginWord])
#     pathFound = False 

#     noBacktrack = set()
#     noBacktrack.add(beginWord)
    
#     chars = 'abcdefghijklmnopqrstuvwxyz'

#     while queue and not pathFound: 
#         # print('queue: ', queue)
#         add_to_noBacktrack = set()
#         for _ in range(len(queue)):                                         # do this so you only append 
#             curPath = queue.popleft()
#             # print('curpath: ', curPath)
#             word1 = curPath[-1]
#             if word1 == endWord: 
#                 res.append(curPath)
#                 pathFound = True
#                 continue
#             for i in range(len(word1)):
#                 for c in chars:
#                     newWord = word1[:i] + c + word1[i+1:]                
#                     if newWord in wordList and newWord not in noBacktrack and dist[newWord] >= dist[word1]:
#                         newPath = curPath + [newWord]
#                         queue.append(newPath)
#                         dist[newWord] = dist[word1] + 1
#                         add_to_noBacktrack.add(newWord)

#             # for word2 in wordList:
#             #     if word2 not in noBacktrack and dist[word2] >= dist[word1] + 1 and countCompare(word1, word2):
#             #         newPath = curPath + [word2]
#             #         # print('newpath:', newPath)
#             #         dist[word2] = dist[word1] + 1
#             #         queue.append(newPath)
#             #         add_to_noBacktrack.add(word2)
#         for x in add_to_noBacktrack:
#             noBacktrack.add(x)
#     return res

# beginWord = "hit" 
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "cet"
# endWord = 'ism'
# wordList= ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"]

beginWord = "aaaaa"
endWord = 'ggggg'
wordList= ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]
print(len(wordList))

print(findLadders(beginWord, endWord, wordList))

# wordTree= bfs(beginWord, endWord, wordList)
# print(bfs(beginWord, endWord, wordList))
# print(dfs(beginWord, endWord, wordTree))


# def findLadders(beginWord, endWord, wordList):
#     res = []
#     wordList = set(wordList)
#     wordList.add(beginWord)
#     if endWord not in wordList:
#         return res
#     graph = defaultdict(set)
    
#     for word1 in wordList: 
#         graph[word1] = set()
#         for word2 in wordList:
#             if word1 == word2: continue
#             counter = 0
#             for i in range(len(word1)):
#                 if word1[i] == word2[i]: counter +=1
#             if counter == len(word1) - 1: graph[word1].add(word2)
#     # print(graph)

#     queue = deque()
#     startingPath = OrderedDict()
#     startingPath[beginWord] = None
#     queue.append((beginWord, startingPath))
#     pathFound = False

#     while queue and not pathFound: 
#         for _ in range(len(queue)):     # do this so you only append 
#             word1, curPath = queue.popleft()
#             # print('popped: ', word1, curPath)
#             if word1 == endWord: 
#                 res.append([key for key in curPath])
#                 pathFound = True
#                 continue
#             for word2 in graph[word1]:
#                 if word2 not in curPath :
#                     newPath = OrderedDict()
#                     for x in curPath:
#                         newPath[x] = None
#                     newPath[word2] = None
#                     queue.append((word2, newPath))
#     return res