import random
def number_guessing_game():
# nếu không có while True thì ct chỉ chạy 1 lần except ValueError sau đó sẽ báo lỗi 
 while True:
    try:  
       low = int(input('Nhập vào khoảng số muốn đoán: \n'))
       high = int(input())
       
       while low >= high:
          print('vui lòng nhập lại')
          low = int(input())
          high = int(input())
          if low < high:
              break
              
       while True:
        try:   
          number = random.randint(low, high)
          chances = int(input('số cơ hội đoán:'))
          chance = chances

          while chances >0:
                guess = input("nhập vào 1 số nguyên: ")
                
                
                try:
                    integer = int(guess)
                    if integer == number :
                        if chances==chance:
                            print('Chúc mừng!!!')
                            print('wow bạn đoán đúng với chỉ 1 lần đoán')
                        else:    
                            print('Chúc mừng!!!')
                        
                        
                        return
                    elif integer in range(low,high+1) and integer < number:
                        if chances >2:
                            print('hãy đoán số lớn hơn')
                            
                            
                        if chances ==2 :
                            print('hãy đoán số lớn hơn')
                            print('bạn chỉ còn 1 cơ hội')
                    elif integer in range(low,high+1) and integer > number:
                        if chances >2:
                            
                            
                            print('hãy đoán số nhỏ hơn')
                        
                        if chances ==2 :
                            print('hãy đoán số nhỏ hơn')
                            print('bạn chỉ còn 1 cơ hội')
                    else:
                        print(f'số bạn đoán 0 nằm trong khoảng {low}-{high}')
                        chances +=1
                    
                        

                except ValueError:
                
                    print("Bạn phải nhập vào 1 số nguyên.")
                    chances +=1
                
                chances -=1
            
        
          print("bạn không đoán đúng lần nào trong {chance} cơ hội. Bạn thua rồi."\
.format(chance=chance))
          print('số cần đoán là:',number)
          return

            
        except ValueError:
            print('cơ hội phải là số nguyên')
        


    except ValueError:
        print('bạn phải nhập vào 1 số nguyên')
number_guessing_game()



#Cách 2: hoan toan tu lam

import random
def guessing():
	while True:
		try:
			low = (int)(input('so thap:'))
			high = (int)(input('so ca0:'))
			if low >= high:
				print('nhap lai')
				low = (int)(input('so thap:'))
				high = (int)(input('so ca0:'))
			if low < high:
				break
		except ValueError:
			print('phai la so nguyen')
		
	found = True
	while True:
		try:
			doan_so = random.randrange(low, high+1) # phai import random module
			co_hoi = (int)(input('so co hoi:'))
			co_hoi_max = co_hoi
			while co_hoi > 0:
					try:
						x = (int)(input('nhap vao 1 so:'))
						if x not in range(low,high+1):
							print('x khong thuoc khoang {}-{}'.format(low,high))
							co_hoi +=1
						if x in range(low, high+1):
							if x < doan_so:
								if co_hoi == 1:
									print('loser');print('so can doan la:',doan_so)
									found = False
									break
								print('doan so cao hon',x)
					
							if x > doan_so:
								if co_hoi == 1:
									print('loser');print('so can doan la:', doan_so)
									found = False
									break
								print('doan so thap hon', x)

							if x == doan_so:
								if co_hoi_max == co_hoi:
									print('wowwwww, doan dung voi 1 lan duy nhat')
									found = False
									break
								print(True)
								found = False
								break
						co_hoi -= 1
					except ValueError:
						print('0 hop le lan 2')
		except ValueError:
			print('0 hop le')
		if found == False:
			break
	
guessing()

#cách3 :
import random

def number_guessing_game():
 x = True
 while True:
    try:  
       low = int(input('Nhập vào khoảng số muốn đoán: \n'))
       high = int(input())
       
       while low >= high:
            
          print('vui lòng nhập lại')
          low = int(input())
          high = int(input())
          if low < high:
              break
              
       
       y = True
       while True:
        try:   
          number = random.randint(low, high)
          chances = int(input('số cơ hội đoán:'))
          chance = chances

          while chances >0:
                guess = input("nhập vào 1 số nguyên: ")
                try:
                    integer = int(guess)
                    if integer == number:
                        print('Chúc mừng!!!')
                        return
                    elif integer in range(low,high) and integer < number:
                        print('hãy đoán số lớn hơn')
                        if chances ==2 :
                            print('bạn chỉ còn 1 cơ hội')
                    elif integer in range(low,high) and integer > number:
                        print('hãy đoán số nhỏ hơn')
                        if chances ==2 :
                            print('bạn chỉ còn 1 cơ hội')
                    else:
                        print(f'số bạn đoán 0 nằm trong khoảng {low}-{high}')
                        chances +=1
                        if  chances ==2:
                            print('bạn chỉ còn 1 cơ hội')
                except ValueError:
                
                    print("Bạn phải nhập vào 1 số nguyên.")
                    chances +=1
                
                chances -=1
            
        
          print("bạn không đoán đúng lần nào trong {chance} cơ hội. Bạn thua rồi."\
.format(chance=chance))
          print('số cần đoán là:',number)
          return

        except ValueError:
            print('cơ hội phải là số nguyên')
        
    except ValueError:
          
          print('bạn phải nhập vào 1 số nguyên')