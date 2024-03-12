// 위의 코드는 “matrix”라는 이름의 6x6 matrix를 내포된 루프의 조건에 기초한 값으로 초기화한다.
// 외부 루프는 행렬의 행에 반복되고 내부 루프는 열에 반복된다.
// row = 열, col = 행
#include <stdio.h>

int row, col, matrix[6][6];

for (row = 0; row < 6; row++) 
{
	for (col = 0; col < 6; col++)
	{
		if (row < col) // 현재 열이 현재 행(즉, 위치가 행렬의 위쪽 삼각형에 있음)보다 작으면 해당 위치의 값이 1로 설정된다.
			matrix[row][col] = 1;
		else if (row == col) // 현재 행이 현재 열과 같으면(즉, 위치가 행렬의 대각선에 있으면) 해당 위치의 값은 0으로 설정된다.
			matrix[row][col] = 0; 
		else // 현재 열이 현재 행보다 크면(즉, 위치가 행렬의 아래 삼각형에 있는 경우) 해당 위치의 값은 -1로 설정된다.
			matrix[row][col] = -1;
	}
}

// 행렬은 대각에 0이 있고 다른 행렬은 -1과 1이 있는 대칭 행렬이다.
// 행렬의 위쪽 삼각형에는 1s가 포함되고 아래쪽 삼각형에는 -1s가 포함된다. 이러한 유형의 행렬을 “삼각행렬”이라고 한다.
