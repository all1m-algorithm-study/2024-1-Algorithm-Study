//갖고 있는 랜선 개수 k개 (1~10000)만큼 입력을 받고,
//필요한 랜선 개수 n개로 쪼갤때 (1~1,000,000)
//만들 수 있는 최대 랜선 길이를 출력하자.

// '길이를 최대화'
// 랜선의 길이를 늘리다보면, T F가 바뀌는 지점이 생기므로
// '단조성'이 있으니까 "이분탐색"으로 활용할 수 있다.

//right는 영식이가 가진 랜선 중 가장 긴 랜선이 길이다.
//주어진 랜선에서 몇개를 찾을 수 있는지 합 now를 구한다.
//찾은 랜선의 개수(now) >= n라면, 랜선의 개수를 줄여야 하므로 mid를 늘린다.
//만들 수 있는 랜선의 가장 큰 값을 찾기 위해 result와 mid 중 큰 값을 result에 저장한다.
//랜선의 개수가 아직 부족하면 mid의 길이를 줄여야 하므로, right = mid -1을 한다.


#include <iostream>
#include <algorithm>

using namespace std;
long long n, k;
long long mid;
long long arr[10000]; //자료형 크기 체크
long long result;

//가능한지 아닌지 확인하는 함수
int valid(long long x) {
    //몫의 합을 저장하는 변수
    //랜선의 길이가 2^31-1보다 작거나 같은 자연수이므로 오버플로우 가능.
    long long now = 0;
    
    for (int i=0;i<k;i++) {
        now += arr[i]/mid;
    }
    
    if (now>=n) return 1;
    else return 0;
}

int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);

    //입력 받기
    long long max_L = -1;
    cin >> k >> n;
    for (int i=0 ; i<k; i++) {
        cin >> arr[i];
        max_L = max(max_L, arr[i]);
    }

    // 이분 탐색
    long long left=1; //최장 길이가 0이 될 수 없으며, 탐색을 0부터 시작하면, divByZero 발생 가능
    long long right = 2147483647; //2^10-1
    long long ans;
    
    while(left<=right) {
        mid = left-(left-right)/2; //(l+r)/2
        if (valid(mid)) {
            left = mid+1;
            // [!] N보다 크거나 같은 개수만큼 자를 수 있는 최대 길이를 찾는 것이다.
            // 즉, valid하면서 가장 큰 값을 result로 넣어주자.
            result = result<mid ? mid : result;
        } else {
            right = mid-1;
        }
    }

    cout << result << endl;
}