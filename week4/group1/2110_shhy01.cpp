//집 N개 각각의 좌표가 x1, x2, ..., xn이다.
//한 집에 공유기 하나만 설치할 수 있고,
//가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치하고자 한다.
//C개의 공유기를 N개의 집에 설치하여, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

//집의 개수 N (2~200,000)
//공유기 개수 C (2~N)
//집의 좌표를 나타내는 x_i(0~1,000,000,000)

//타당하게 하면서 최대로 갖게 하는 값을 찾고자 한다.

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, C;
int mid; //가장 인접한 두 공유기 사이의 거리를 찾기 위한 변수
int result; //가장 인접한 두 공유기 사이의 거리

vector<int> position;

int solve() {
    int left=1; //두 공유기 사이의 최소 거리 : 1
    int right=position[N-1]-position[0]; //두 공유기 사이의 최대 거리 : 첫집 ~ 끝집
    
    while(left <= right) {
        mid = (left + right)/2;

        //[!] 공유기는 어디에 두지?

        //첫번째 공유기는 설치하고 시작
        int install_router_cnt = 1; 
        int start = position[0];

        for (int i=1; i<N; i++) {
            //간격 확인할 공유기 위치
            int end = position[i];

            //공유기 간격이 기준 간격(mid)를 넘는다면, valid하므로 설치한다.
            if ( (end - start) >= mid) {
                install_router_cnt++;
                start = end; //방금 설치한 라우터 기준으로 다시 추가 공유기 설치해보자.
            }
        }

        //공유기 간격 탐색이 끝난 뒤,
        //설치한 공유기 개수가 C개 이상이라면,
        if (install_router_cnt >= C) {
            //문제 조건을 만족하므로, 현재 구한 공유기 간격을 결과로 임시 저장.
            result = max(result, mid);
            //문제 조건을 만족하면서 더 공유기 간격을 늘릴 수 있는지 확인해보자. 
            left = mid + 1;
        }
        //설치한 공유기 개수가 C개 미만이라면,
        else {
            //공유기 간격을 더 좁혀서 공유기 설치가 더 가능하도록 하자.
            right = mid - 1;
        }
    }

    return result;
}

int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);

    cin >> N >> C;
    int num;
    for(int i=0; i<N; i++) {
        cin >> num;
        position.push_back(num);
    }

    sort(position.begin(), position.end());
    
    cout << solve() << endl;
    return 0;
}