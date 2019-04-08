def Main(N, arr):
		arr.sort() # 對門牌號碼做排序(小至大)
		d = 0 # 為相加總和
		if N%2: # 若數量為奇數，則中位數為陣列的中間值
			mid = arr[N//2]
		else:  # 若數量為偶數，則中位數為中間的兩數擇一，或是兩數取平均
			mid = 0.5*(arr[N//2 - 1] + arr[N//2])
			
		for a in arr: # 將距離相加，並回傳
			d += abs(a - mid)
			
		return int(d)

if __name__ == '__main__':
	T = int(input())  # T為測資數量
	for _ in range(T): # 讀入每一行測資
		arr = list(map(int, input().split())) # 對每一行測資做切分、轉型(str to int)，並存至陣列(arr)中
		print(Main(arr[0], arr[1:])) # 呼叫Main函數並輸出函數回傳結果，其中arr[0]代表親戚數，arr[1:]代表接續輸入的多個門牌號碼
