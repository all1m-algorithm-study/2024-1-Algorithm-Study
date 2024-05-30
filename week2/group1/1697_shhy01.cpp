//https://www.acmicpc.net/problem/1697

//나는 현재 점 N(0~100,000)에 있고, 상대는 점 K(0~100,000)에 있다.
//내 현재 위치가 X라면, 1초 후에 이동하는 방법은 X+1 / X-1 혹은 2*X 중 하나이다.
//내가 상대의 위치를 가장 빨리 찾는 시간이 몇초인지 찾아보자.

//현재 위치 N부터 시작해서, 이동 방법 3가지에 따른 하위 노드를 만들면서, K를 얻을 때까지 진행하면 되겠다. -> BFS

#include <bits/stdc++.h>
using namespace std;

int N, K;
int result_time;
bool visited[100000]; //이미 방문한 노드라면 다시 탐색할 필요 없음.

bool isValid(int location) {
    if (location>=0 && location<=100000) return true;
    return false;
}

void BFS(int N) {
    queue<pair<int, int>> Q;
    Q.push(make_pair(N, 0));

    while(!Q.empty()){
        int x = Q.front().first;
        int cnt = Q.front().second;

        Q.pop();
        if(x==K) {
            cout << cnt;
            break;
        }
        if(isValid(x+1)) {
            if(!visited[x+1]) {
                visited[x+1] = true;
                Q.push(make_pair(x+1, cnt+1));
            }
        }
        if(isValid(x-1)) {
            if(!visited[x-1]) {
                visited[x-1] = true;
                Q.push(make_pair(x-1, cnt+1));
            }
        }
        if(isValid(x*2)) {
            if(!visited[x*2]) {
                visited[x*2] = true;
                Q.push(make_pair(x*2, cnt+1));
            }
        }
    }
}
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> K;

    BFS(N);

    return 0;
}