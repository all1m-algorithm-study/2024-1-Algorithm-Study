//knapsack problem
//부피가 K인 배낭, N개의 물건이 있다.
//각 물건은 부피

// [X] 그리디 접근 : 가치가 큰 것, 부피가 작은 것, 쪼개서 담기, ... 성립 불가
// [X] 완전 탐색 : 물건 개수 N개에 따른 경우의수 2로, O(2^N)이므로 절대 불가능

// [!] 같은 무게에 대하여, 가치가 더 높은 것을 선택하는 것이 좋다.
// 최대 부피 K를 가지는 문제의 답은 : Max(부피가 1일때 최대 가치, 2일때 최대 가치, ... , K일 때 최대 가치)
// 이때 부피가 i일 때 최대 가치는 부피가 Max(a<i일때 최대 가치 + i-a일 때 최대 가치)로 다시 쪼개질 수 있겠다.
// 

//N개의 물건을 한번에 처리하는건 복잡.
//1. dp(i,v) = i번째까지 물건을 봤을 때 부피 v에 들어가는 최대 가치 값
//2. i번째 물건을 넣었을 때 / 넣지 않았을 때로 구분
// 넣었다면 dp(i+1, v+무게)+가치
// 안넣었다면 dp(i+1, v)

#include <bits/stdc++.h>

using namespace std;

int N, K;
int W[101], V[101];
int DP[101][100001]; //DP[i][w] : 부피 i까지 고려했을 때의 가치 w

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    //input
    cin >> N >> K;
    for (int i=1 ; i<=N ; i++) {
        cin >> W[i] >> V[i];
    }
    
    //knapsack
    for(int row=1; row<=N ; row++) {
        for(int limit=1; limit<=K; limit++) {
            //아이템이 남은 무게 weight보다 작다면, 아이템을 담을 수 있다.
            if(W[row] <= limit)
                DP[row][limit] = max(DP[row-1][limit - W[row]] + V[row], DP[row-1][limit]);
            else //담을 수 없는 경우라면,
                DP[row][limit] = DP[row-1][limit];
        }
    }
    cout << DP[N][K] << endl;
}