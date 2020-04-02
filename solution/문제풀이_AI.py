
#quiz1


'''
11. 최대공약수를 구하는 함수를 구현하시오
'''''
def gcd(a,b):
    i = min(a,b) # a 와 b 중에서 최솟값을 찾는다.
    while True: #조건식이 만족할 떄 까지 계속 무한루프를 돌린다.
        if a % i==0 and b % i==0: # a 와 b를 i로 나누었을때 나머지가 0이면
            return i # i를 반환하는 하고
        i = i -1 # 둘다 나머지가 0 이 아니면 i의 수를 1씩 낮춰서 다시 루프를 돌린다.


'''
 - 유클리드 호제법 -
큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체한다.
큰 수를 작은 수로 계속 나누어서, 나누어 떨어질 때까지 반복한다. 나누어 떨어질 때(나머지가 0일 때), 나누는 수가 최대공약수이다
'''

def gcd2(a,b):
    n = max(a,b) # 최댓값 찾기
    m = min(a,b) # 최솟값 찾기
    while (n % m ) != 0: #  n / m 의 나머지가 0 이 아니면
         s = n % m  #s라는 변수는 n / m 의나머지로 변환
         n = m #n은 m으로 변환
         m= s #m은 S로 변환
    return m # while 문 조건이 만족되는 m 값 반환


'''
15.
주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을
작성하시오. (리스트 split 과 슬라이싱 활용)
'''
num = input("주민등록번호 : ").split("-") # input 으로 주민등록번호를 받는데 -를 기준으로 끊는다.
                                         # 943310-1003254  를 입력하면 ['943310','1003254'] 로 적용
se = num[1] # 리스트중 2번쨰 리스트
if(se[:1] == "1" or se[:1] == "3"): #se 첫번쨰 값이 1이거나 3이면
    print("남자") #남자를 출력
elif(se[:1] == "2" or se[:1] == "4"): # #se 첫번째 값이 2이거나 4이면
    print("여자") # 여자 출력
#----------------------------------------------------- 밑에처럼 해도 상관없음.
if se[0] == "1" or se[0] == "3":
    print("남자")
elif se[0] == "2" or se[0] == "4":
    print("여자")


#알고리즘

'''
2.첫 번째 숫자를 두 번째 숫자부터 마지막 숫자까지 차례대로 비교하여
가장 작은 값을 찾아 첫 번째에 놓고,  두번째 숫자를 세 번째 숫자부터
마지막 숫자까지 차례대로 비교하여그 중 가장 작은 값을 찾아
두 번째 위치에 놓는 과정을 반복하며 정렬하는것을 선택정렬이라고 합니다.
주어진 리스트를 선택정렬함수(select_sort)를 생성하여 오름차순으로 정렬하시오

'''

list=[6,2,3,7,8,10,21,1]

def select_sort(a):
    n = len(a) # 리스트의 길이를 잰다.
    for i in range(0,n-1): # i 의 변수는 0부터 7까지
        min_idx = i  #min_idx = 0
        for j in range(i+1,n):  #j의 변수는 1 ~ 7
            if a[j] < a[min_idx]: # a[1] = 2 이고 a[0] = 6   2 < 6 이므로
                min_idx = j # min_idx 의 값이 0 에서 1로 변경
        a[i] , a[min_idx] = a[min_idx],a[i]  # 비교하다보면 min_idx는 7이되고 i는 0이니까 자리바꿈 - > 리스트가 [1,2,3,7,8,21,6] 이됨 다시 첫번째 for 문으로 돌아감.
    return a

print(select_sort(list))


'''
3.앞뒤로 이웃한 숫자를 비교하여 크기가 큰 숫자가 작은숫자보다 앞에 있을
경우 서로 위치를 바꿔 가며 정렬하는 것을 버블정렬이라고 합니다.
주어진 리스트를 버블정렬함수(bubble_sort)를 생성하여 오름차순으로 정렬하시오.
'''

list=[4,3,2,1,8,7,5,10,11,16,21,6]
def bubble_sort(a):
    for j in range(len(a)-1,0,-1): # j값은 리스트의 길이 12-1 인 11 부터 하나씩 줄어듬
        for i in range(j): #i=0 ~ 10
            if a[i] < a[i+1]: #a[0] = 4 이고 a[1] 은 3 이니 조건 반족 안해서  else로 넘어감
                continue
            else:
                a[i],a[i+1] = a[i+1],a[i] # 0번째와 1번째 자리바꿈.
    return a


print(bubble_sort(list))


'''

4.탐욕 알고리즘은 최적해를 구하는 상황에서 사용하는 방법입니다.
여러 경우 중 하나를 선택할 때 그것이 그상황에서 가장 좋다고 생각하는 것을
선택해 나가는 방식으로 진행하여 답을 구합니다.
하지만 탐욕알고리즘은 그 상황에서 가장 좋다고 생각하는 것을 선택해 나가는
방식이기 때문에 가장 좋은 결과를 얻는 것이 보장되는것은 아닙니다.
탐욕 알고리즘을 이용하여 동전을 지불하는 함수(greedy)를 짜는데 지불해야 하는
동전의 갯수가 최소가 되도록 함수를 구현하시오
(input 으로 액수와 동전의 종류를 입력하게 구현)

'''
def greedy():
    b =[]
    money = int(input('액수입력 : '))
    cash_type = [int(x) for x in input('동전의 종류 : ').split(' ')] #띄어쓰기로 끊어서 리스트로 저장
    cash_type.sort(reverse =True) #동전의 종류를 뒤죽박죽 입력할  수도 있으니 내림차순으로 정렬
    for i in range(len(cash_type)):
        b.append('%s원 동전 %s개' %(cash_type[i], money // cash_type[i]))  #b라는 리스트에 append 시키는데 금액을 첫번째 캐쉬타입으로 나누었을때의 몫을 삽입
        money =money - ((money // cash_type[i]) * cash_type[i]) # money의 변수를 변경 -> 560원을 입력하고 cash_type의 첫번째 값이 100이라하면
                                                                # 560 - ( (560 //100) *100) = 60 으로 변경
    x=', '
    answer=x.join(b) # b라는 리스트값을 , 로 구분하여 출력
    return answer

print(greedy())
