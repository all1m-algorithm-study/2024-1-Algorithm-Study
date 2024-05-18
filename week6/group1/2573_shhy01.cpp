#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <queue>

#define MAX 300
using namespace std;

int N, M;
int MAP[MAX][MAX];
int toMelt[MAX][MAX];
bool visited[MAX][MAX];

//정익 멘토님의 조언 !!
//[?] : 문제 주어진 그대로 구현을 했는데, 내 알고리즘은 시간 초과 문제가 없을까?
//[!] : 문제 조건을 보아, 주어지는 정수는 0 이상 10 이하이고, 1 이상의 정수가 들어가는 칸의 개수는 10000개이다.
//예를 들어 100x100의 모두 10으로 채워진 input을 생각해보면,
//예상 최대 반복 횟수는 50*10*10=5000번이고,
//이는 주어진 제한 시간 1초 안에 계산 가능함.

//좌우상하 방향을 표현.
int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

// BFS 함수 정의
void BFS(int a, int b) {
    queue<pair<int, int>> q;
    q.push(make_pair(a, b)); //첫 노드를 queue에 삽입
    visited[a][b] = true; //첫 노드를 방문 처리

    //큐가 빌 때까지 반복
    while (!q.empty()) {
        //큐에서 하나의 원소를 뽑아 출력
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for (int i = 0 ; i < 4; i++) {
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];
            
            if (nx >= 0 && ny >= 00 && nx < N && ny < M) {
                if (visited[nx][ny] == 0 && MAP[nx][ny] !=0) {
                    visited[nx][ny] = true;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
}

void melt(int n, int m) {
    //빙산 녹기전 녹아야 할 양 카운트
    for(int i=0; i<n; i++) {
        for(int j=0; j<m;j++) {
            for (int k=0; k<4; k++) {
                int nx = i + dir[k][0];
                int ny = j + dir[k][1];

                if (MAP[nx][ny] <= 0)
                    toMelt[i][j]++;
            }
        }
    }
    //빙산 녹이기
    for(int i=0; i<n;i++) {
        for(int j=0; j<m;j++) {
            if( MAP[i][j] > 0 ) MAP[i][j] -= toMelt[i][j];
            //빙산이 녹으면 0이하로 되는 경우 처리.
            if( MAP[i][j] < 0 ) MAP[i][j] = 0;
        }
    }
}

void solve() {
    int year= 0; //빙산이 분리되는 최초의 시간(년)
    while(1) {
        int LandSet_cnt = 0;
        memset(visited, false, sizeof(visited));
        memset(toMelt, 0, sizeof(toMelt));

        
        //BFS 탐색.
        //그래프 하나로 모든 빙산 탐색이 불가능하면, 빙산이 두 덩어리 이상인 것이다.
        for (int i=0;i<N;i++) {
            for (int j=0;j<M;j++) {
                if (MAP[i][j] != 0 && visited[i][j]==false)
                {
                    //방문하지 않은 데이터를 찾았다면
                    LandSet_cnt++; //먼저 빙산 덩어리 개수 카운트 증가해두고,
                    BFS(i,j); //주어진 입력 데이터 탐색.
                }
            }
        }

        //빙산이 2개 이상으로 분리되었다면, 걸린 시간(년) 출력
        if (LandSet_cnt >= 2) {
            cout << year << '\n';
            break;
        }
        //빙산이 다 녹을 때까지 분리되지 않으면 0을 출력
        if (LandSet_cnt == 0) {
            cout << 0 << '\n';
            break;
        }

        //위의 2가지 경우에 해당하지 않는다면, 빙산 녹이기
        melt(N,M);
        year++;

    }
}

int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);
    
    //input
    cin >> N >> M; //행, 열
    for (int i=0;i<N;i++) { //주어지는 정수
        for (int j=0 ; j < M ; j++) {
            cin >> MAP[i][j];
        }
    }
    
    //solution
    solve();
    return 0;
}

