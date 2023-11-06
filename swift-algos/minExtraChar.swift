// iterate across each string in the dictionary
// if str is in the string, remove it, go to the next leftover 

// -- add that string to a set so that you 
// -- do you add that string to the set or do you add the leftover of that string? 

func minExtraChar(_ s: String, _ dictionary: [String]) -> Int {

    var stringArr = Array(s)

    class Trie {
        var word = false 
        var children = [String.Element: Trie]()
    }

    let wordSearch = Trie()

    // build the wordSearch by inserting words in the trie
    for word in dictionary {
        var curWordSearch = wordSearch
        
        // insert each letter in the trie structure
        for (_, x) in word.enumerated() {
            if curWordSearch.children[x] == nil {
                curWordSearch.children[x] = Trie()                
            }
            curWordSearch = curWordSearch.children[x]!
        }
        curWordSearch.word = true          // at the end of the for loop, tag the word as true
    }
    
    // traverse the trie 
    func printChar(_ curTrie: Trie) {
        if !curTrie.children.isEmpty {
            for key in curTrie.children.keys {
                // print(key)
                printChar(curTrie.children[key]!)
            }
        }
    }

    // print all words in the trie 
    func printWord(_ curTrie: Trie, _ s: String) -> Void {
        // print(s)
        if curTrie.word == true {
            print(s)
        }
        if !curTrie.children.isEmpty {
            for key in curTrie.children.keys {
                printWord(curTrie.children[key]!, "\(s)\(key)")
            }
        }
    }

    // get all of the words that start with a char c 
    func getArr(_ curTrie: Trie, _ s: String) -> [String] {
        var res = [String]()

        func dfs(_ curTrie: Trie, _ s: String) {
            if curTrie.word == true {
                res.append(s)
            }
            if !curTrie.children.isEmpty {
                for key in curTrie.children.keys {
                    dfs(curTrie.children[key]!, "\(s)\(key)")
                }
            }
        }

        dfs(curTrie, s)

        return res
    }

    // let wordArr: [String] = getArr(wordSearch.children["s"]!, "s")

    // print("printing...")
    // print(wordArr)
    // printWord(wordSearch, "")

    // res
    var res = [Int]()
    for _ in 0..<s.count + 1{
        res.append(0)
    }

    // start i from the end of the string to 0
    // then for each i, check if  
    print("scount: ", s.count)
    print("res: ", res)
    for i in stride(from: s.count - 1, through: 0, by: -1) {
        print(i)
        res[i] = res[i + 1] + 1
        // check if the ith string is in the wordsearch. 
        // if it is, then start iterating across the children in the tree. 
        // if at any point you reach a tree that's true and you get a string, 
        // then make res[i] = min(res[i], res[i + fullwordfound.count])

        let curString = stringArr[i]
        if let childrenTrie = wordSearch.children[curString] {
            let wordArr: [String] = getArr(childrenTrie, String(curString))
            
            for word in wordArr {
                if word.count 
            }

        }



    }

    return 3
} 



// var s = "abcde"
// var dictionary = ["a", "b", "c", "d"]

var s = "leets"
var dictionary = ["leet", "code", "lea", "leat", "scode"]

// print(min(3, 4))

print(minExtraChar(s, dictionary))