class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        if not len(s) or not len(p):
            return not len(s) and not len(p)
        table = [False for _ in xrange(len(p) + 1)]
        table_prev = [False for _ in xrange(len(p) + 1)]
        table[0] = True
        for p_end in xrange(1, len(p) + 1):
            if p[p_end - 1] == '*':
                table[p_end] = table[p_end - 1]

        for s_end in xrange(1, len(s) + 1):
            table_prev, table = table, table_prev
            table[0] = False
            for p_end in xrange(1, len(p) + 1):
                if p[p_end - 1] == '*':
                    table[p_end] = table[p_end - 1] or table_prev[p_end]
                elif p[p_end - 1] == '?':
                    table[p_end] = table_prev[p_end - 1]
                else:
                    table[p_end] = s[s_end - 1] == p[p_end - 1] and table_prev[p_end - 1]
        return table[-1]


if __name__ == '__main__':
    print Solution().isMatch("accaacaabcc", "*acc*")