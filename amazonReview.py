import os

data = []
count = 0

with open('reviews.txt','r',encoding='utf-8') as f:
    for line in f:
        data.append(line)
        count += 1
        # if count % 1000 == 0:
        #     print(len(data))
print('檔案讀取完畢，總共有',len(data),'筆資料')


wc = {} # word count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] +=1
        else:
            wc[word] = 1 #新增新的key進wc

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))


while True:
    input_word = input('請輸入要查詢的單字:')
    if input_word == 'q':
        break
    if input_word in wc:
        print(input_word, "一共出現了", wc[input_word], "次")
    else:
        print(input_word, "沒有出現過")

print('感謝使用本查詢功能')


# total_length = 0
# num_reviews = len(data)

# for review in data:
#     total_length += len(review)

# average_length = total_length / num_reviews if num_reviews > 0 else 0

# print(f'總共有{num_reviews}筆評論')
# print(f'平均每筆評論有{average_length:.2f}個字')

