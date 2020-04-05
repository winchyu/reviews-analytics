#GitHub 教學濃縮:
    # 上傳/更新檔案上GitHub
    # 都要執行 git 指令三部曲:
    # git add 檔名
    # git commit -m "版本訊息"
    # git push origin master

print('---------------------------','\n')

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


data = [] 
with open('reviews.txt', 'r') as f:
    for line in f:  
        data.append(line) 
        # print(len(data)) # 每讀一筆，就計算一筆
        # 很花時間，可以改成每1000 筆，計算一次

print('---------------------------','\n')

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





