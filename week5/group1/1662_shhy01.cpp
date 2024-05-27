#include <string>
#include <iostream>

using namespace std; // 표준 라이브러리에 정의된 클래스와 함수들을 std::를 붙이지 않고 사용하도록 한다.

string str; // 입력으로 받을 문자열 변수 선언

// 스택 또는 재귀로 풀 수 있다.
// 문자열의 왼쪽부터 탐색하므로, 재귀 함수를 인덱스 0부터 시작한다.
// 1. 0부터 오른쪽 끝까지 탐색하면서, 현재 문자가 숫자라면 길이 증가
// 2. 현재 문자가 (라면 방문 체크를 하고, 재귀 함수를 호출
// 3. 현재 문자가 )라면 방문 체크를 하고, cnt 반환

// 문제 분석 -> 문제 입력 크기(복잡도)
// 재귀 -> 수학적 귀납법
// 괄호 처리 unzip

//15650 17478 - 함수호출 스택에 넣고 반환

bool visited[50]; //각 문자의 방문 여부를 저장.

int recur(int idx) {
	int cnt = 0;
    //idx는 탐색을 시작할 문자열의 인덱스
	//(!) index가 괄호의 끝을 가리켜야 다시 방문하지 않으므로, index가 공유돼야 겠다.

	for (int i = idx; i < str.length(); i++) {
		char ch = str[i];
		//open : 현재 문자가 열린 괄호이고, 아직 방문하지 않은 경우
		//방문체크를 하고, cnt는 열린 괄호 왼쪽 수와 return값을 곱해 더해줘야 한다.
		if (ch == '('&& !visited[i]) {
            // 열린 괄호 다음의 숫자를 가져와,
            // 그 수만큼 재귀적으로 다음 문자를 탐색한다.
			visited[i] = true;
			cnt--;
			cnt += (int)(str[i - 1] - '0') * recur(i+1);
		}
		//close : 닫힌 괄호를 만나면
		else if (ch == ')'&& !visited[i]) {
			visited[i] = true; //인덱스를 방문 처리하고
			return cnt; //현재까지 계산한 문자열 길이를 반환한다.
		}
		//num
		else if(!visited[i]) {
			visited[i] = true; //방문 처리를 하고
			cnt++; //괄호 내 문자열 길이를 증가한다.
		}
	}
	return cnt;
}

int main() {

    //입력을 빠르게 받기 위해, 버퍼를 비운다.
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
    // 입력으로 문자열을 받아서, str에 저장하고
	cin >> str;
    // recur함수를 호출하여 문자열의 개수를 계산하여 출력한다.
	cout << recur(0);

	return 0;
}