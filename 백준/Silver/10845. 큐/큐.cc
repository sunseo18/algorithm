#include <iostream>
#include <string>
using namespace std;

#define MAX_SIZE	100000
int queue[MAX_SIZE];
int frnt = 0;
int rear = 0;
int empty() {
	if (frnt == rear) return 1;
	else return 0;
}
void push(int x) {
	rear = (rear + 1) % MAX_SIZE;
	queue[rear] = x;
}
int pop() {
	if (!empty()) {
		frnt = (frnt + 1) % MAX_SIZE;
		return queue[frnt];
	}
	else return -1;
}
int size() {
	if (empty()) return 0;
	else if (rear > frnt) return rear - frnt;
	else return rear + MAX_SIZE - frnt;
}
int front() {
	if (!empty())
		return queue[(frnt + 1) % MAX_SIZE];
	else return -1;
}
int back() {
	if (!empty())
		return queue[rear];
	else return -1;
}
int multiTen(int y) {
	if (y == 0) return 1;
	else if (y == 1) return 10;
	else {
		int result = 1;
		for (int i = 0; i < y; i++) {
			result *= 10;
		}
		return result;
	}
}
int main() {

	int number, data;
	string s;
	cin >> number;
	getchar();
	for (int i = 0; i < number; i++) {
		getline(cin, s);

		if (s == "front") {
			cout << front() << endl;
		}
		else if (s == "back")
			cout << back() << endl;
		else if (s == "empty") {
			cout << empty() << endl;
		}
		else if (s == "size") {
			cout << size() << endl;
		}
		else if (s == "pop") {
			cout << pop() << endl;
		}
		else {
			data = 0;
			for (int i = 5; i < s.length(); i++) {
				char a = s[i];
				data += (a - '0') * multiTen(s.length() - (i + 1));
			}
			push(data);
		}
	}
}