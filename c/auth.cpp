#include <iostream>
#include <string>
//#include <windows.h>
#include <locale.h>
using namespace std;
int main() {
    setlocale(LC_ALL, "RUSSIAN");
    string a;
    string b;
    cout << "Введите Логин и Пароль" << endl;
    cout << "Логин:";
    cin >> a;
    cout << "Пароль:";
    cin >> b;
    if (a == "Player1" && b == "1234") {
        cout << "Добро пожаловать!" << endl;
    }
    if (a != "Player1" || b != "1234") {
        cout << "Неверный логин или пароль" << endl;
	return 0;
    }
    if (a == "Player2" && b == "12345") {
        cout << "Добро пожаловать!" << endl;
	return 0;
    }
    if (a !=  "Player2" || b != "12345") {
        cout << "Неверный логин или пароль" << endl;
        return 0;	
    }
    //system("PAUSE");
    return 0;
}

