def cover_rate( str1, str2):
    # 计算str1在str2中的覆盖率
    def findall(body, sub, start=0):
        result = []
        while True:
            pos = body.find(sub, start)
            if pos >= 0:
                result.append(pos)
                start = pos + len(sub)
                # body = body[pos+len(arg):]
                continue
            break
        return result

    poss = findall(str1, " ")  # str1中“ ”出现的位置
    word_count = len(poss) + 1
    for pos in poss:
        if str1[0:pos] in str2:
            continue
        else:
            return poss.index(pos)/word_count
    if str1 in str2:
        return 1
    else:
        return (word_count - 1)/word_count

print(float(cover_rate("<h1>teekay tankers ltd.</h1>","teekay tankers ltd. reports first quarter 2018 results")))