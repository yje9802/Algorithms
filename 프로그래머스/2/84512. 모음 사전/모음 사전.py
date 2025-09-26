def solution(word):
    answer = 0
    
    word_dict = [] # 사전("A", "AA", "AAA", ...)
    words = "AEIOU"
    
    def dfs(cnt, curr_word):
        if cnt == 5:
            return
        for i in range(5):
            new_word = curr_word + words[i]
            word_dict.append(new_word)
            dfs(cnt+1, new_word)
    
    dfs(0, "") # 처음에는 빈 문자열부터 시작
    answer = word_dict.index(word) + 1
    return answer