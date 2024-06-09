//https://www.acmicpc.net/problem/1780

//단순히 같은 수로 모이게 종이를 자르는 것이 아니라,
//종이가 모든 같은 수로 되어 있지 않다면, 9등분을 하고, 다시 등분된 종이 조각이 각각 모두 같은 수로 되어 있는지 확인하면 된다.
//따라서, 쉽게 '재귀', 'Divide and Qonquer'를 떠올릴 수 있을 것이다.

#include <bits/stdc++.h>

using namespace std;

int arr[2187][2187];
int cnt_minus, cnt_zero, cnt_plus; //-1, 0, 1로 채워진 종이 개수

//함수에 들어갈 매개변수에 대한 고민이 있었는데, 이 안에서 지역 변수를 만들어 계산하면 되겠다.
bool check_to_cutting_or_not(int y, int x, int size) {
    int factor = arr[y][x]; //배열의 첫 원소 넣기 주의
    for (int i=y; i<y+size ; i++) {
        for (int j=x; j<x+size ; j++) {
            if (factor != arr[i][j]) return true; //cut
        }
    }
    return false; //not cut
}

void div(int y, int x, int size) {
    if (!check_to_cutting_or_not(y, x, size)) { //종이 내의 숫자가 모두 같다면, 카운트한다.
        if (arr[y][x] == -1) cnt_minus++;
        if (arr[y][x] == 0) cnt_zero++;
        if (arr[y][x] == 1) cnt_plus++;
    }
    else { //종이 내의 숫자가 모두 같지 않다면, 종이를 divide한다.
        size = size/3;
        for (int i=0 ; i<3 ; i++) {
            for (int j=0 ; j<3 ; j++) {
                div(size*i+y, size*j+x, size);
            }
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;  //입력되는 정사각형 종이의 가로(세로) 크기 1~3^7
    cin >> N;

    //행렬로 표현되는 종이를 어떻게 표현할 것인가에 대한 고민이 좀 들었는데,
    //편하게 행렬로 쓰자.
    for (int y=0; y<N ; y++) {
        for (int x=0; x<N ; x++) {
            cin >> arr[y][x];
        }
    }

    div(0, 0, N);

    cout << cnt_minus << endl << cnt_zero << endl << cnt_plus;

    return 0;
}