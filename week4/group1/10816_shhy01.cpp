// 숫자 카드 N개를 갖고 있을 때, 정수 M개가 주어지면 이 수가 적힌 숫자 카드를 총 몇개 갖고 있는지 구하자.

// 갖고 있는 카드 개수 N (1 ~ 500,000)
// 정수 N개 (-10,000,000 ~ 10,000,000)
// 주어지는 카드 개수 M
// 정수 M개

//배열이 정렬된 '단조성'을 보이고, 'Random-access'가 가능할 때,
//최적 해를 구하는 "이분 탐색" 적용하기

#include <bits/stdc++.h>

using namespace std;

int N, M;

vector<int> having;
vector<int> reference;

void solve(void){
    
}
int main(void) {
    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(0);
	cin.tie(0);

    //입력 받기
    cin >> N;
    int num;
    for(int i=0 ; i<N ; i++) {
        cin >> num;
        having.push_back(num);
    }
    sort(having.begin(), having.end());

    cin >> M;
    for(int i=0 ; i<M ; i++) {
        cin >> num;
        reference.push_back(num);
    }

    // solve
    // 정렬된 having에 대해서, check에 해당하는 숫자가 몇개 있는지 확인.
    for(int i=0 ; i<reference.size(); i++) {
        //upper_bound() : 찾고자 하는 key보다 큰 값 중 가장 처음 나오는 값의 반복자 반환
        //lower_bound() : 찾고자 하는 key보다 크거나 같은 값 중 가장 처음 나오는 값의 반복자 반환
        cout << upper_bound(having.begin(), having.end(), reference[i]) - lower_bound(having.begin(), having.end(), reference[i]) << ' ';
    }
    return 0;
}