#include <stdio.h>
#define ARRAY_SIZE	5
// 이것은 ARRAY_SIZE (크기는 5)로 정의된 정수 숫자 배열을 선언하는 프로그램 이다.
// 그런 다음 inputNumbers와 computeAverage라는 두 가지 함수를 호출합니다.

void inputNumbers(int num[], int len);
double computeAverage(int num[], int len);

void inputNumbers(int num[], int len)
// inputNumbers 함수는 int num 와 int len 이라는 두 가지 인수를 사용한다.
// 사용자에게 int len의 값을 입력하라는 메시지가 표시되며, 이 정수는 ARRAY_SIZE 에 저장됩니다.
{
	int i;
	for (i = 0; i < len; i++) // 사용자에게 len의 길이의 수 만큼 scanf를 이용해서 입력을 받고, 그 값을 저장한다.
		scanf("%d", &num[i]);
}

double computeAverage(int num[], int len)
// computeAverage 함수는 int num 와 int len의 두 가지 인수도 사용한다. ARRAY_SIZE 에 있는 숫자의 평균을 계산하고 이를 반환한다.
{
	int total = 0;
	int i;
	for(i = 0; i < len; i++) // 배열의 개수를 len 만큼 받아온다. 그리고 평균을 계산, 배열을 돌려서 출력 한다. for & scanf
		total = total + num[i];
	return total / (double)len;
}

int main()
{
	int numbers[ARRAY_SIZE];
	
	inputNumbers(numbers, ARRAY_SIZE);
	printf("average: %.3lf", computeAverage(numbers, ARRAY_SIZE));
	// 마지막으로 inputNumbers 함수를 호출하여 값을 채운 다음 computeAverage 함수를 호출하여 배열에 있는 숫자의 평균을 계산.
	// 결과는 printf를 사용하여 소숫점 3자리 까지 출력시킨다.

	return 0;
}
