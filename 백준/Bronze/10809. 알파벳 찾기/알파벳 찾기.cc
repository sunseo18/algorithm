#include<iostream>
using namespace std;
int main() {
	
	string st;
	int length = 0, alpha[26];
	cin >> st;

	for (int i = 0; i < 26; i++) alpha[i] = -1;

	for (int i = 0; st[i] != '\0'; i++) length++;
	
	for (int i = 0; i < length; i++) {
		for (int j = 0; j < 26; j++) {
			if ((int)st[i] == j + 97) {
				if(alpha[j] == -1) alpha[j] = i;
				break;
			}
		}
	}
	
	for (int i = 0; i < 26; i++) {
		cout << alpha[i] << ' ';
	}
}