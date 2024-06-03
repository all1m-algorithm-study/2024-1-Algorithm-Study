//2xN 타일에 2x1 타일을 알맞게 넣는 방법의 가지수를 찾는 문제

//2xN 타일 경우의 수를 dp[n]이라고 두자.

//2xN 타일 경우의 수를 계산하는 방법을 생각해보면,
//2x(N-1)에 2x1 타일을 붙이는 방법과, 2x(N-2)에 2x2 타일을 붙이는 방법이 있다.

//즉, dp[n] = dp[n-1] + dp[n-2]이다.
//따라서, 이전에 계산한 결과를 배열에 저장하면 용이하다.

//이는 끝이 2x1 혹은 2x2로 되는 경우 두가지이다.

//1. 하향식 DP (Top-Down)
//재귀함수를 이용
//dp(n,m) -> dp(n-1,m)

//2. 상향식 DP (Bottom-Up)
//반복문을 이용
//dp(0,0), dp(0,1), ..

#include <iostream>

using namespace std;

int dp[1001];
int tile(int k) {
    if (k==1) return 1;
    if (k==2) return 2;
    if (dp[k] > 0) return dp[k]; //배열에 값이 저장되었으면 바로 출력
    dp[k] = tile(k-1) + tile(k-2);
    //n으로 입력받을 수 있는 최대 수가 1000이므로, int나 long long으로 표현할 수 있는 범위를 초과한다.
    //따라서, 오버플로우가 발생하지 않기 위해 10007로 나눈 나머지를 저장한다. (문제에서 제시됨.)
    dp[k] %= 10007;
    return dp[k];
}

int main(void) {

    int n;
    cin >> n;

    cout << tile(n);
    return 0;
}