#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    string ra, login, pass, rpass, rlogin, clogin, cpass;
    cout << "Hello!" << endl << "register/authorize(r/a): ";
    cin >> ra;
    if (ra == "r")
    {
        cout << "login: ";
        cin >> rlogin;
	if (rlogin =="admin")
	{
		cout << " nezzya!" << endl;
	}
        cout << "password: ";
        cin >> rpass;
	int wlen = rpass.length ();
	//while (wlen < 8)
	//{
	//	cin >> rpass;
	//	cout << " nezzya!" << endl;
	//}
        ofstream flogin("login.txt");
        flogin << rlogin;
        flogin.close();
        ofstream fpass("pass.txt");
        fpass << rpass;
        fpass.close();
    };
    if (ra == "a")
    {
        cout << "...reading..." << endl;
        ifstream flogin("login.txt");
        ifstream fpass("pass.txt");
        while (!flogin.eof() & !fpass.eof())
        {
            flogin >> clogin;
            fpass >> cpass;
        };
        cout << "login: ";
        cin >> login;
        cout << "password: ";
        cin >> pass;
        fpass.close();
        flogin.close();
        if (login == clogin & pass == cpass)
        {
            cout << "ready!" << endl;
        }
        else if (login != clogin)
         {
            cerr << "Error: invalid login" << endl;
            system("pause");
        }
        else if(pass != cpass)
        {
            cerr << "Error: invalid password" << endl;
            system("pause");
        };
    };
    if (ra != "a" & ra != "r")
    {
        cerr << "Fatal error: invalid value" << endl;
        system("pause");
    };
    system("pause");
}

