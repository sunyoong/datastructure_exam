import stack
from bracket import *

# odd = stack.Stack()
# even = stack.Stack()


# for i in range(10): # 1부터 9까지
#     if i%2 == 0:
#         even.push(i)
#         print(i)
#     else:
#         odd.push(i)
#         print(i)  
        
# #print('odd 출력 : ', odd.top)
# #print('even 출력 : ', even.top)


# print('__str__ 구현 후 odd  : ', odd)
# print('__str__ 구현 후 even : ', even)
# print('__str__ 역순으로 구현 후 odd  : ', odd)
# print('__str__ 역순으로 구현 후 even : ', even)

result = bracket("{int i, tmp=score[0]; for(i=1; i<n; i++){if(score[i]>tmp) {tmp = score[i];}}return tmp;}")
print(result)
