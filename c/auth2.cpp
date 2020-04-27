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
	//string passw1;
        cout << "password";
	//if (passw1.length() < 8)
	//{	
	//	cout << " is not correct";
	//	return 1;
	//}
	//else
	//{
	cin >> rpass;
        ofstream flogin("login.txt");
        flogin << rlogin;
        flogin.close();
        ofstream fpass("pass.txt");
        fpass << rpass;
        fpass.close();
   // };
   // if (rpass.leght() < 8)
//	{
//		cout << " is not correct";
//		return 1;
//	};

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
        };
        else if (login != clogin)
         {
            cerr << "Error: invalid login" << endl;
	    return 0;
        };
        else if(pass != cpass)
        {
            cerr << "Error: invalid password" << endl;
	    return 0;
        };
    };
    if (ra != "a" & ra != "r")
    {
        cerr << "Fatal error: invalid value" << endl;
    };
    return 0;
}

