//https://www.acmicpc.net/problem/30985



//K층으로 구성, 각 층은 방과 복도로 구성
//복도를 통해 방과 방 사이를 양방향으로 이동할 수 있다.
//모든 층은 같은 모습을 하고 있다.

//파댕이는 1층의 1번 방에 있고, 목표지점은 K층의 N번 방이다.
//현재 위치에서 목표지점까지 최소 시간을 쓰도록 하자.

//'복도'라는 개념이, 두 정점을 잇는 간선의 가중치로 생각하고,
//'방'이라는 개념을 정점으로 생각하면
//초기 위치 -> '엘리베이터'가 있는 방 -> K층의 N번방으로 이동이 가장 단순한 경로일 것이다.
//최소 시간을 구하면서, 양의 가중치만 고려하기 때문에 '다익스트라'를 적용해보면 되겠다.

#include <bits/stdc++.h>
#define ll long long

using namespace std;

vector <pair<ll, ll>> graph[101010];

ll N, dp[2][101010] = {0};

void dij(ll x) {
    priority_queue <pair <ll, ll>, vector <pair <ll, ll> >, greater<> > q;

    ll node; //시작 노드

    if (x == 0) node = 1; //1층부터 시작하는 경우와
    else node = N; //

    for (ll i=1 ; i<=N ; i++)
        dp[x][i] = 1e18;

    dp[x][node] = 0; //시작 노드의 최단 거리는 0으로 설정    
    q.push({0, node}); //시작 노드를 큐에 삽입

    while(q.size()) { //큐가 빌 때까지
        ll distance = q.top().first; //현재 노드까지의 최단 거리
        ll temp_num = q.top().second; //현재 노드 번호

        q.pop(); //큐에서 현재 노드 빼기

        //이미 더 짧은 경로가 있으면 패스
        if (dp[x][temp_num] < distance) continue; 

        //현재 노드와 인접한 노드들에 대하여 탐색.
        for (auto i : graph[temp_num]) { // 현재 노드와 인접한 정점 v에 대하여
            ll d = i.second + distance; // (현재 노드, v)의 가중치
            ll now = i.first; //인접 노드 v의 번호
            if (d < dp[x][now]) { //v의 distance가 u의 distance + w보다 크다면, 최단 경로 갱신
                dp[x][now] = d; //최단 시간 테이블 갱신
                q.push({d, now}); // 큐 삽입
            }
        }
    }
}
int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ll M, K;
    cin >> N >> M >> K;

    //복도 정보
    ll u, v, c;
    for(int i=0 ; i<M ; i++) {
        cin >> u >> v >> c;
        //양방향으로 이동 가능한 복도임을 고려
        graph[u].push_back({v , c});
        graph[v].push_back({u , c});
    }

    dij(0); dij(1);//1층에서 시작하는 경우와, K층에서 시작하는 경우의 최단 거리를 각각 계산

    ll result = 1e18;

    //각 방의 엘리베이터 유무를 입력 받는다.
    for(int i=1 ; i<=N ; i++) {
        ll x;
        cin >> x;

        //엘리베이터가 없으면 바로 다음으로 넘기고
        if (x==-1) continue;
        //엘리베이터가 있다면, 단축된 시간을 구한다.
        result = min(result, x*(K-1) + dp[0][i] + dp[1][i]);
    }

    //기록을 단축했다면, result 출력하고, 아니면 -1을 출력
    if (result != 1e18) cout << result;
    else cout << -1;
}