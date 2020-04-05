#GitHub 教學濃縮:
    # 上傳/更新檔案上GitHub
    # 都要執行 git 指令三部曲:
    # git add 檔名
    # git commit -m "版本訊息"
    # git push origin master

print('---------------------------','\n')

# 01
data = [] 
with open('reviews.txt', 'r') as f:
    for line in f:  
        data.append(line) 
print(len(data)) 

# print(data) 會印出一百萬筆資料
print(data[0]) # 印出第一筆留言

print('---------------------------','\n')

print(data[1])

print('---------------------------','\n')

# 02
data = [] 
with open('reviews.txt', 'r') as f:
    for line in f:  
        data.append(line) 
        # print(len(data)) # 每讀一筆，就計算一筆
        # 很花時間，可以改成每1000 筆，計算一次

print('---------------------------','\n')

# 03
data = [] 
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:  
        data.append(line) 
        count += 1 # count = count + 1 的快寫法
        # 每讀一筆就加一
        if count % 1000 == 0: # 當count 與1000 的餘數為0
        # % 是用來求餘數
            print(len(data)) 
            # 如果count 與1000 求餘數是0，才計算一筆
            # 就會每1000筆，才計算一筆

print(len(data)) 

print('---------------------------','\n')

# 04
data = [] 
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:  
        data.append(line) 
        count += 1 # count = count + 1 的快寫法
        # 每讀一筆就加一
        if count % 1000 == 0: # 當count 與1000 的餘數為0
        # % 是用來求餘數
            print(len(data)) 
            # 如果count 與1000 求餘數是0，才計算一筆
            # 就會每1000筆，才計算一筆

print('檔案讀取完了，總共有', len(data), '筆資料')

print('---------------------------','\n')

# 05
data = [] 
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:  
        data.append(line) 
        count += 1 # count = count + 1 的快寫法
        # 每讀一筆就加一
        if count % 1000 == 0: # 當count 與1000 的餘數為0
        # % 是用來求餘數
            print(len(data)) 
            # 如果count 與1000 求餘數是0，才計算一筆
            # 就會每1000筆，才計算一筆

print('檔案讀取完了，總共有', len(data), '筆資料')

# 6
sum_len = 0
for d in data:
    sum_len += len(d) 
    # sum_len = sum_len + len(d)
print(len(data[0]))    
print(len(data[1]))
print(len(data[2]))
print(len(data[3]))
print(len(data[4]))
print(len(data[5])) 
print('留言的總長度為', sum_len)

print('留言的平均長度為', sum_len/len(data))

print('---------------------------','\n')

# 7
new = []
for d in data: 
# for loop 的意思就是，
# 把清單中的東西一個一個拿出來
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')        
print(new[0])
print(len(new[0])) # new[0] 的長度包括每個字母，標點，空白在內

print(new[1])
print(len(new[1]))

print('---------------------------','\n')

