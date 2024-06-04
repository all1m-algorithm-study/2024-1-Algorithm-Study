//세미나 배정
//세미나 N개를 주최

//각 세미나는 연속된 T일 동안 진행되어야 한다.
//구체적으로, m을 정해야 하며, i번째 세미나는 m일부터 m+T-1일차까지 매일 진행된다.
//각 세미나의 T일 중 하루(a)는 외부전문가의 특강이 진행된다. 즉, m <= a <= m+T-1

//하루에 가장 많이 진행되는 세미나 수를 최소화하고 싶다.
//즉, 반대로 생각해보면
//동시에 진행되는 세미나를 i개로 두고, 이를 만족하면서 가장 작은 i가 정답이 된다.

//배열이 정렬된 '단조성'을 보이고, 'Random-access'가 가능할 때,
//최적 해를 구하는 "이분 탐색" 적용하기 -> O(N log N)으로 해결 가능.

#include <iostream>
#include <algorithm>

using namespace std;

int N; //(1~200,000)
int T; //(1~1,000,000,000)
int arr[200001] = {0};
int dp[200001] = {0};
long long mid;
int result;

//고정으로 넣어야 하는 날짜인 a를 기준으로,
//T일의 세미나 일정을 넣을 수 있는 경우의 수를 DP로 파악해보자.

//DP 풀이의 3단계
//1. 상태공간을 정의한다. : 완전 탐색(brute force)과정에서 중복되어 나타나는 부분을 잘 포괄할 수 있도록 잡자.
//2. 상태공간 사이의 관계식을 구한다.
//3. Memorization을 활용해 코드를 작성한다.


//하루에 최대 mid개의 세미나가 배정되는 것이 True/False?
int temp_cnt(long long mid) {
    //먼저, 고정으로 들어가야 할 세미나 날짜를 차례대로 넣는다.
    for (int i=0 ; i < N ; i++) dp[i] = arr[i]; 

    if (mid == 0) return false;
    
    //mid개의 세미나를 배정해보자.
    for (int i=0 ; i < N ; i++) {
        //일단 i<mid인 i번째 세미나는 최대한 먼저 시작하도록 한다. 
        if (i < mid) {
            //dp[i]에는 각 세미나의 시작 날짜를 넣자.
            dp[i] = max(arr[i] - T + 1, 1);
            continue;
        }
        //i >= mid인 i번째 세미나는 앞서 들어갔을 (i-mid)번째 세미나의 시작 시간 + T와 비교해서 넣는다.
        dp[i] = max(dp[i - mid] + T, max(arr[i] - T + 1, 1));
    }
    //i번째 세미나의 특강 날짜보다 시작 날짜가 뒤면, 말이 안됨. False 반환
    for (int i=0 ; i < N ; i++) {
        if (dp[i] > arr[i]) return false;
    }
    //이상 없으면 True 반환
    return true;
}

int solve() {
    //이분 탐색
    long long left=0;
    long long right=200001;

    while(left+1 < right) {
        mid = left-(left-right)/2;
        if (temp_cnt(mid)) {
            right = mid;
        } else {
            left = mid;
        }
    }

    return right;
}

int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);
    cin >> N >> T;

    for (int i=0; i<N; i++) {
        cin >> arr[i]; // (1~1,000,000,000)
    }
    
    sort(arr, arr+N); //입력 받은 전문가특강 날짜를 순서대로 정렬.

    cout << solve() << endl;
}