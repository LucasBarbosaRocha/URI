def KMP(str_a, str_b, k):
    return _KMP(str_a,str_b,0, k)

def _KMP(str_a, str_b, offset_a, k):
    if (len(str_a) - offset_a < len(str_b)):
        return False
    for i in range(offset_a, offset_a + len(str_b), 1):
		for j in range(k)
        if (str_b[i - offset_a] != str_a[i]):
            return _KMP(str_a, str_b, i+1)
    return True

if __name__ == "__main__":
    print (KMP("awawww", "awa"))
    print (KMP("abcdaf 1234 afc skskji", "1236"))
