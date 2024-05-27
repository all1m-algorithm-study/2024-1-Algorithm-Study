#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define MAX 25
using namespace std;

//정사각형 모양의 지도. 집이 있는 곳은 1, 없는 곳은 0.
//연결된 집(좌,우,상,하)의 모임인 단지를 정의하고, 번호를 붙인다.

//입력 : 지도의 크기 N, 그리고 N*N 지도(0,1)
//출력 : 단지 수, 각 단지에 속하는 집의 수

int MAP[MAX][MAX];
int visited[MAX][MAX];
int N;
int cnt;//각 단지 내 집의 수 계산하는 temp 변수
vector <int> result; //각 단지 집의 수를 저장하는 변수
//좌우상하 방향을 표현.
int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};


// BFS 함수 정의
void BFS (int a, int b) {
    queue<pair<int, int>> q;
    q.push(make_pair(a, b)); //첫 노드를 queue에 삽입
    visited[a][b] = true; //첫 노드를 방문 처리
    cnt++;

    //큐가 빌 때까지 반복
    while (!q.empty()) {
        //큐에서 하나의 원소를 뽑아 출력
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        //해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for(int i=0 ; i<4 ; i++) {
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];

            //0 ~ N-1의 배열을 쓰므로 범위 주의!
            if (nx >=0 && ny>= 0 && nx < N && ny < N) {
                if (visited[nx][ny] == 0 && MAP[nx][ny] != 0) {
                    visited[nx][ny] = true;
                    q.push(make_pair(nx,ny));
                    cnt++;
                }
            }
        }
    }
}

void solve() {
    //BFS 탐색
    for (int i=0 ; i<N ; i++) {
        for (int j=0 ; j<N ; j++) {
            if (MAP[i][j] != 0 && visited[i][j] == false) {
                //방문하지 않은 데이터를 찾았다면,
                cnt = 0;
                BFS(i, j); //주어진 입력 데이터 탐색.
                result.push_back(cnt);
            }
        }
    }
    //문제 조건에 따라 오름차순 정렬
    sort(result.begin(), result.end());

    cout << result.size() << '\n';
    for (int i=0 ; i<result.size() ; i++) {
        cout << result[i] << '\n';
    }
}
int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);
    
    //input
    cin >> N; //행(열)
    //주어지는 정수 입력 주의
    for (int i=0;i<N;i++) {
        string input;
        cin >> input;
        for (int j=0 ; j < N ; j++) {
            MAP[i][j] = input[j] - '0';
        }
    }
    
    //solution
    solve();
    return 0;
}

