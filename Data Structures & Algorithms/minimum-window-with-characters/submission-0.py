class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return

        count_T, window = {}, {}

        for c in t:
            count_T[c] = count_T.get(c, 0) + 1
        
        have, need = 0, len(count_T)
        res, res_len = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_T and window[c] == count_T[c]:
                have += 1
            
            while have == need:
                #update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                
                #pop from left of window
                window[s[l]] -= 1

                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        if res_len != float("infinity"):
            return s[l : r + 1 ]
        else:
            return ""

            






    
                


               


            





            
            
                
     

           


        


        