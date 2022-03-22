# before the Lesson
car = input('請問是否開過車：')
age = input('請問您的年齡：')
age = int(age) # 未轉換型別
if car == '是': # ==要兩個，不知為何？
	if age < 18:
		print('打咩，壞寶寶')
	elif age >= 18 and age < 80:　＃要冒號，且大小於常打錯！另外and後面的主詞age要再打一次！
	    print('不要當三寶')
	elif age >= 80:
		print('盡量不要開車哦')
else:
	print('滿18就可以學開車了哦')

# after
driving = input('請問你有沒有開過車？')
    # (※詳下面)可以加上:
    if driving != '有' and '沒有':
    	print('只能輸入 有/沒有')
    raise SystemExit #直接讓系統中斷運行
age = input('請問你的年齡？')
age = int(age)
if driving == '有': 
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了，怎麼還不去考')
    else:
    	print('很好，再過幾年就可以考駕照了')
else: # 所有以外的回答>>>※也可以加在上面，這行就可以刪除
	print('只能輸入 有/沒有')