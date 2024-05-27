#include <iostream>

using namespace std;

// 재귀 함수를 사용할 때 접근 법.
// 1/ 탈출 조건이 될 때까지 실행한다.
// 2. 일정 규칙을 찾고 구현한다.
// 3. 제일 큰 과정을 염두하고 구현하면, 나머지는 자동으로 된다.


// 입력 : 첫번째 장대에 쌓인 원판의 개수
// 출력 : 옮긴 횟수 출력 후, 수행 과정(from, to 장대 위치) 출력

void hanoi(int from, int via, int to, int n) {
    //이동할 원판의 수가 1개일 때(탈출 조건)
    if (n==1) {
        cout << from << ' ' << to << '\n';
        return;
    }
    hanoi(from, to, via, n-1); // 1 -> 2 번째 장대로 원판을 n-1개 옮김.
    cout << from << ' ' << to << '\n'; // 가장 큰 원판을 목적 지점으로 옮김.
    hanoi(via, from, to, n-1); // 2 -> 3 번째 장대로 n-1개를 옮김.
}

int hanoiCnt(int n) {
    if (n==1) return 1;
    return 2 * hanoiCnt(n-1)+1;
}

int main() {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

    int n;
    cin >> n;
    cout << hanoiCnt(n) << '\n';
    hanoi(1, 2, 3, n);
}