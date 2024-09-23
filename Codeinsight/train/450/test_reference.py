def test(var0):
    max_substring = ""
    for i in range(len(var0)):
        for j in range(i + 1, len(var0)):
            substring = var0[i:j]
            next_occurrence = var0.find(substring, j)
            if next_occurrence >= j and len(substring) > len(max_substring):  # Ensure no overlap and the substring is longer
                max_substring = substring
    return max_substring

