def ritm(text):
    lst_1 = list(text.split())
    vowels = set('уеаоэяиюыё')
    for i in range(len(lst_1)):
        count = 0
        for letter in lst_1[i]:
            if letter in vowels:
                count += 1
            lst_1[i] = count
    if len(set(lst_1)) == 1:
        return "Парам пам-пам"
    return "Пам парам"
text = 'парам пам-паме'
print(ritm(text))