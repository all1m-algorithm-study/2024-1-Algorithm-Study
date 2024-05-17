#include <iostream>
#include <cmath>

using namespace std;

//자연수 A를 B번 곱한 수(거듭제곱)를 알고 싶다.
//이를 C로 나눈 나머지를 구하는 프로그램을 작성해라.

// * 문제 접근 *
// 1. 입력이 2,147,483,647 이하의 자연수이므로, long long을 쉽게 넘긴다.
// -> Divide & Conquer
// b가 짝수라면, a^b = a^(b/2) * a^(b/2)
// b가 홀수라면, a^b = a^(b/2) * a^(b/2+1)

long long cal(long long a, long long b, long long c) {
    if (b == 0) return 1;

    long long temp;
    temp = cal(a, b/2, c); // 지수를 절반 나눠서 호출
    temp = temp*temp%c; //c로 나눈 나머지를 temp에 저장
    if (b % 2 == 0) return temp; //짝수라면 그대로
    else return temp*a%c; //홀수라면, a를 곱해서 다시 c로 나눈다.

}

int main() {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

    long long a, b, c;
    cin >> a >> b >> c;
    cout << cal(a,b,c);

    return 0;
}