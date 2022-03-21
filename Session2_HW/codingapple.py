print(1111)
print('나' *100)

이름 = '드래곤'
print(이름)
# 등호 : 오른쪽 데이터를 왼쪽에 집어넣으라

print(이름[0])

car = ['K5', 'white', [5000, 6000]]

print(car)
print(car[1])

car[1]='black'
print(car)

# list.sort() : 숫자/문자순 정렬
# list.reverse() : 리스트 순서 바꿈
# list.pop()

# dictionary
car2 = {
    'brand':'BMW', 
    'model':'520d'
    }
    
print(car2)
print(car2['brand'])

# 자료수정
car2['brand'] = 123
print(car2['brand'])


left = 10

if left>0:
    print('지금주문가능합니다')

중고차재고 = ['K5', 'BMW', 'Tico']
if 'K5' in 중고차재고:
    print('지금주문가능합니다')

중고차들 = ['K5', 'BMW', 'Tico']

for car in 중고차들:
    print(car)