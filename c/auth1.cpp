//#include <conio.h>
#include <string>
#include <iostream>
#include <vector>

void sign_in() 
{
    std::string       login;
    std::vector<char> password;

    char c;

    std::cout << "Enter login: ";
    std::cin >> login;
    std::cout << "Enter password: ";
    while ((c = _getch()) != '\r')
    {
        password.push_back(c);
        _putch('*');
    }

    std::cout << std::endl << login << " : ";

    for (std::size_t i = 0; i < password.size(); ++i)
        std::cout << password[i];
    std::cout << std::endl;
}

int main(int argc, char* argv[])
{
    sign_in();

    return EXIT_SUCCESS;
}
