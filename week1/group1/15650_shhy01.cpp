#include <bits/stdc++.h>

using namespace std;

int n, m;
int arr[10];
bool isused[10];

// N과 M이 주어졌을 때,
// 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
// 1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
// 2. 고른 수열은 오름차순이어야 한다.

// '백트래킹'

// 비어있는 리스트에서 수를 하나씩 추가하면서,
// 길이가 M인 수열이 완성되면 출력하는 식으로 구현.

void func(int x, int y) { //현재 k개까지 수를 택했다.
    if(x==m) { //m개를 모두 택했다면
        for(int i = 0; i<m; i++)
            cout << arr[i] << ' '; //arr에 기록해둔 수를 출력
        cout << '\n';
        return;
    }

    for (int i=y; i<=n; i++) { //1부터 n까지의 수에 대해
        if(!isused[i]) { //아직 i가 사용되지 않았다면
            arr[x] = i; //k번째 수를 i로 정함
            isused[i] = 1; //i를 사용되었다고 표시
            func(x+1,i+1); //다음 수를 정하러 한 단계 더 들어감
            //k번째 수를 i로 정한 모든 경우에 대해 다 확인했으니,
            //i를 이제 사용하지 않았다고 명시함.
            isused[i] = 0; 
        }
    }
}

int main() {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(false);
	cin.tie(0);

    cin >> n >> m;
    func(0,1);
}