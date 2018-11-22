6_28_ex3.py
==============

![default](https://user-images.githubusercontent.com/44903476/48913283-45ac1280-eebb-11e8-9336-85bd752713c3.png)
2018년도 여름계절에 수강하였던 파이선 프로그래밍의 과제 문제에 대한 코드이다.

- 각 층에 해당하는 숫자에 맞춰서 1호라인에서 4호라인까지가 이진수로 표현되어 있는 꼴이다.

````
num1 = int(input())
num2 = int(input())

num3 = num1 & num2
num4 = num1 | num2

num3 = bin(num3)
num4 = bin(num4)

print(num3.count('1'))
print(num4.count('1'))
````

* 비교할 두개의 층을 num1과 num2에 입력 받기 위하여 input을 이용하였다.

* 입력 받은 두 수를 &를 이용하여 각 bit끼리 and 연산을 한 값을 num3에 저장하였고 |를 이용하여 각 bit끼리 or연산을 한 값은 num4에 저장하였다.
````
5&8의 경우
5 = 0101
8 = 1000
5&8 = 0000
5|8 - 1101 이 출력된다.
````

* 그 후 bin을 이용하여 num3와 num4의 값을 2진수로 변환하였다.

* 마지막으로 변환된 2진수의 값의 1의 갯수를 출력하기 위해 count를 이용하였다.
- count : 특정 원소의 개수를 찾을 때 사용한다.

````
※ 주의할 점
l2 = [1,2,[1,2]] 일 때
l2안에 2라는 원소가 있기에 l2.count(2)의 결과값은 1이다.
여기서 [1,2]자체를 하나의 원소로 보기에 [1,2]안의 2는 l2.count(2)에 포함되지 않는다.
l2[2].count(2)의 결과값도 1이다.
이는 l2[2]가 index가 2인 원소, 즉 [1,2]를 나타내고 그 원소 내에서 2인 원소의 개수를 구하는 것이기에 결과값이 1이 나온다.
````

* 결론적으로 num3에는 입력된 두개의 층에서 둘다 불이 켜져있는 경우의 호 라인을 2진수 형태로 나타낸 값이 입력되어 있으며 num4에는 입력된 두개의 층 중 하나라도 불이 켜져있는 호 라인을 2진수 형태로 나타낸 값이 입력되어 있게 된다.
