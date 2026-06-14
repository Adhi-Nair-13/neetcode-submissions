class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        
        # 2. Loop through each original word in the input list
        for word in strs:
            # Sort the word alphabetically. 
            # sorted("cat") gives ['a', 'c', 't']. We use "".join() to turn it back into a string: "act"
            sorted_key = "".join(sorted(word))
            
            # 3. Throw the original word into its matching bucket
            buckets[sorted_key].append(word)
            
        # 4. Return just the groups of words, ignoring the sorted keys
        return list(buckets.values())