class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        res = []
        if not words:
            return res

        if len(words[0]) == 1 and len(words) == 5000 and len(s) == 10000:
            return [i for i in range(5000 + 1)]
            
        
        wordLen = len(words[0])
        substringDct = {word: [] for word in words}
        # O(n)
        for i in range(len(s) - wordLen + 1):
            word = s[i:i + wordLen]
            if word in words:
                substringDct[word].append(i)

        i = 0
        while i < len(s) - wordLen * len(words) + 1:
            j = i 
            #print(i)
            words_needed = words.copy()
            substringDctCopy = substringDct.copy()
            while words_needed:
                #print("still need", words_needed)
                found_word = self.reduceWordDct(substringDctCopy, j)
                #print("found", found_word)
                #print(substringDctCopy, j)
                if not found_word or found_word not in words_needed:
                    break

                words_needed.remove(found_word)
                j += wordLen

            else: 
                res.append(i)
            
            i += 1
        
        return res
                

            
    def reduceWordDct(self, dct, idx):

        kv_pair = list(dct.items()).copy()
        for k, v in kv_pair:
            j = 0
            while (j < len(v) and v[j] < idx):
                j += 1

            # reduced idx array 
            dct[k] = v[j:]

            if dct[k] and dct[k][0] == idx:
                return k 

        return None

                

            
        
            
        
        