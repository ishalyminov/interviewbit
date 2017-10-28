class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        B = set(B)
        lengths = set(map(len, B))
        matrix = [False for _ in xrange(len(A) + 1)]
        for i in xrange(1, len(A) + 1):
            if matrix[i] == False and A[0:i] in B:
                matrix[i] = True

            if not matrix[i]:
                continue

            if i == len(A):
                return 1
            for j in xrange(i + 1, len(A) + 1):
                if matrix[j] == False and j - i in lengths and A[i: j] in B:
                    matrix[j] = True
                if j == len(A) and matrix[j]:
                    return 1
        return 0


if __name__ == '__main__':
    print Solution().wordBreak('myinterviewcoach', ['my', 'interview', 'coach'])
    # print (Solution().wordBreak("aaaabaababaaaabaabbabbbbbabaabbbbabbbabaabbabaaaaaabaabbabbbaabaababaabbaaabaababbaabbbaabaaaaabbbbaaaaabaababbbababbabbaabbbbabababaababaaaababbbaaaaaaabbbbaabbbbabbbabbbaaabbaaaaabbbabaaaabbababbbbaababaabaababbbbababbbaaaabbbbaabbbaaaabaababbbaaaaaabbbabbaaabaabaabaaaababbbabbbabbbaabbabaaabaaabbababaabbabaaaabbbbbbabbababaaabbababbabbaaaabbabbbababbbbaabaaabbbaababababaaaaaaaabababaabbabaaabbabaaaaaabbbbbbabaaabbaaaaaaaabbbbabbaaabaabbabbbbbbbbbbbbbbabbbababbbbaabaaabaababbaaabbbbaaabbbbbaabababbaabbabbaaabaababbbbbaaaaabbbabaabaaaabaaaaababbabbababbbbbbaaababbbbbbbabbaabbabaaabbbaabbabaaaabaababb", [ "aabababaa", "aaaabaa", "ababaabaa", "aaaa", "b", "aaaaba", "a", "aaba", "bbaaaaaab", "bbb", "aabbaaaaba", "baa", "aabbaba", "abbabb", "bbaaab", "bbbbabbaab", "abbaabbb", "babaa", "b", "bbaaa", "bab", "abaaaaaa", "bbbba", "baababab", "abbaa", "bbaaaaa", "aaaabbbbba" ]))