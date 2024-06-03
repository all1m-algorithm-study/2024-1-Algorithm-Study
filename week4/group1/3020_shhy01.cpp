// https://www.acmicpc.net/problem/3020
// 장애물(석순, 종유석)로 가득찬 동굴.
// 동굴의 길이는 N미터(짝수, 2~200,000), 높이는 H미터(2~500,000이다.

// 첫번째 장애물은 항상 석순, 그다음은 종유석과 석순이 번갈아가며 등장.

// 장애물을 피하지 않고, 지나갈 일직선의 높이를 결정하면, 만나는 장애물을 파괴한다.
// 이때, 동굴의 크기 N과 높이 H, 모든 장애물의 크기가 주어지면,
// 파괴해야 하는 장애물의 최솟값과, 이를 만족하는 구간이 총 몇개인지 구하자.

// [!] 주어진 파괴 수 x 내로 끝내는 것이 가능한가로 해결하면 쉬워지겠다.
// f(x)로 따지면, T와 F가 단조성을 가지므로, '이분 탐색'이 가능하겠다.

// 주의할 사항은, 석순(홀수번째)과 종유석(짝수번쨰)이 번갈아가며 나타난다는 점을 고려하자.

#include <bits/stdc++.h>

using namespace std;

int N, H;

int obstacles_1[100000];
int obstacles_2[100000];

int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);

    cin >> N >> H;
    for (int i=0 ; i<(N/2) ; i++)
        cin >> obstacles_1[i] >> obstacles_2[i];
    
    //이분탐색을 위해, 먼저 정렬을 하자.
    sort(obstacles_1, obstacles_1+(N/2));
    sort(obstacles_2, obstacles_2+(N/2));

    //높이별로 파괴 횟수를 따져보고 가장 최소로 파괴하는 높이를 얻자.
    int min_crush_cnt=200000; //정답 값을 얻어낼 변수
    int valid_height_cnt=0; //최소로 파괴할 수 있는 높이가 몇번 있는가

    for (int i=1 ; i<=H ; i++) {

        //i번째 높이에 대하여, 파괴를 몇번 해야 할 지 계산한다.
        //먼저, 파괴되지 않는 위치를 카운트(cnt)하고, N - cnt해서 구할 것이다.
        int temp_crush_cnt = lower_bound(obstacles_1, obstacles_1+(N/2), i) - obstacles_1; //석순에 대하여, 크기가 i보다 같거나 큰 숫자가 처음으로 등장하는 인덱스를 받는다.(lower_bound - arr)
        temp_crush_cnt += upper_bound(obstacles_2, obstacles_2+(N/2), H - i) - obstacles_2; //종유석에 대하여, 크기가 (H-i)보다 큰 숫자가 처음으로 등장하는 인덱스를 받는다. (upper_bound - arr)
        
        temp_crush_cnt = N - temp_crush_cnt;

        //현재까지 구한 최소 횟수보다 작은 파괴 횟수가 나오면, 업데이트한다.
        if (temp_crush_cnt < min_crush_cnt) {
            min_crush_cnt = temp_crush_cnt;
            valid_height_cnt = 1; //초기화
        }
        else if (temp_crush_cnt == min_crush_cnt) { //현재까지 구한 최소 파괴 횟수와 동일한 파괴 횟수를 갖는 높이가 또 얻어지면, 카운트를 늘린다.
            valid_height_cnt++;
        }
    }
    cout << min_crush_cnt << ' ' << valid_height_cnt;
    return 0;
}
