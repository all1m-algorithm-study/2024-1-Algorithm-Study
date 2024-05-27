#include <iostream>
#include <vector>
#include <string.h>
#include <queue>
#include <algorithm> //sort

using namespace std;

/*
그래프 표현 방식에는 인접 행렬과 인접 리스트가 있다.
인접 행렬은 2차원 배열 형태이고, 인접 리스트는 vector 형태이다.
공간 복잡도 : O(V^2) / O(V+E)
시간복잡도 : 모든 노드 탐색 시 O(V) / O(E)이다.
*/
int N, M, V; //정점의 개수(1~1000), 간선의 개수(1~10,000), 탐색을 시작할 번호 V
// 그다음은 간선이 연결하는 두 정점의 번호가 주어진다. (양방향)

vector<int> vec[1001]; //인접 리스트를 저장할 vector는 정점의 최대 개수가 1000이다.
vector<int> result_bfs;
vector<int> result_dfs;
bool visited[1001]; //정점의 방문 기록할 배열 visited

void BFS(int V){
    queue<int> Q;
    Q.push(V); //처음 방문한 정점 V를 Q에 push
    visited[V] = true; //처음 방문한 정점 V를 방문 기록.

    while(!Q.empty()){ //Q가 빌 때까지
        int cur = Q.front(); //현재 방문한 정점을 'cur'에 저장.
        Q.pop(); //Q에서 'cur' 정점 빼내고,
        result_bfs.push_back(cur); //현재 방문한 정점을 BFS vector에 저장.

        //다음 방문할 정점을 찾는다.
        for(int i=0 ; i<vec[cur].size() ; i++){ //현재 방문한 정점과 이어진 정점의 개수만큼 반복.
            //[!] 단, 방문할 수 있는 정점이 여러개라면, 번호가 낮은 숫자부터 탐색.
            sort(vec[cur].begin(), vec[cur].end()); 
        
            if(!visited[vec[cur][i]]){ //방문하지 않은 곳만 탐색
                Q.push(vec[cur][i]); //다음 정점을 Q에 push.
                visited[vec[cur][i]] = true; //방문 표시.
            }
        }
    }
}
// BFS 함수 정의
void DFS(int V) {
    visited[V] = true; //첫 노드를 방문 처리
    result_dfs.push_back(V); //현재 정점을 BFS에 넣는다.

    //큐가 빌 때까지 반복
    for(int i=0 ; i<vec[V].size() ; i++){
        //[!] 단, 방문할 수 있는 정점이 여러개라면, 번호가 낮은 숫자부터 탐색.
        sort(vec[V].begin(), vec[V].end()); 

        if(!visited[vec[V][i]]){ //방문한 적이 없다면
            DFS(vec[V][i]); //다음 정점을 넘겨주면서 DFS 호출
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0);
	cin.tie(0);

    int N, M, V, from, to;
    
    //input
    cin >> N >> M >> V;
    for (int i=0 ; i<M ; i++) {
        cin >> from >> to;
        vec[from].push_back(to); //양방향 간선처리
        vec[to].push_back(from); //양방향 간선처리
    }

    DFS(V);
    memset(visited, false, sizeof(visited));
    BFS(V);
    for (int i=0 ; i<result_dfs.size() ; i++){
        cout << result_dfs[i] << ' ';
    }
    cout << '\n';
    
    for (int i=0 ; i<result_bfs.size() ; i++){
        cout << result_bfs[i] << ' ';
    }
    return 0;
}