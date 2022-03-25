#include <iostream>
#include <string>
using namespace std;

#define maxSize	10000
int stack[maxSize];
int topp = -1;

int empty() {
	if (topp == -1) return 1;
	else return 0;
}
void push(int x) {
	stack[++topp] = x;
}
int pop() {
	if (!empty()) {
		int data;
		data = stack[topp--];
		return data;
	}
	else return -1;
}
int size() {
	return topp + 1;
}
int top() {
	if (!empty())
		return stack[topp];
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

		if (s == "top") {
			cout << top() << endl;
		}
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
				data += (a - '0')* multiTen(s.length() - (i + 1));
			}
			push(data);
		}
	}
}