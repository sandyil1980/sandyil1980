//#include "stdafx.h"
#include <cstring>
#include <fstream>
#include <iostream>
using namespace std;
int isMax(char mask[], int num, char in[]);        //Функция проверки символа
int main(int argc, char* argv[])
{
    if (argc == 1) {
        cout << "Use PasswordGenerator [Mask] [quantity of passwwords] [Path to file]\n";        //Проверка входных параметров
        return 1;
    }
    ofstream out;            //Выходной файл
    out.open(argv[3]);        //Открываем файл с именем которое ввел пользователь
    int len = 0;                    //Длина пароля
    char mask[1024] = "hll";       //Маска пароля
    char buff[1024] = { 0 };        //Буфер под пароль
    double quant = 0;                //Количество паролей в выходном файле
    strcpy_s(mask, argv[1]);        //копируем маску введённую пользователем
    len = strlen(mask);                //Узнаем длину
    for (int ii = 0; ii < len; ii++) {
        if ((mask[ii]= 'l') && (mask[ii]= 'h')&& (mask[ii]= 'n')) {           //Проверка маски на корректность
            cout << "Mask can be l h n\n";                                        //Маска может содержать только: l маленькие латинские буквы; h большие латинские буквы; n цифры
                return 2;
        }
    }
    quant = atoi(argv[2]);                      //Запоминаем количество комбинаций
    if (quant == 0) {                           //Если пользователь ввел "0"
        quant = 1;                                //То считаем все возможные комбинации
        for (int ii = 0; ii < len; ii++) {         
            switch (mask[ii])
            {
            case 'l': quant *= 26; break;       //26 - количество возможных букв
            case 'h': quant *= 26; break;
            case 'n': quant *= 10; break;       //10 - количество возможных цифр
            default:
                break;
            }
        }
    }
    int ii = 0;        //Нужная переменная
    for (ii = 0; ii < len; ii++) {               //Тут создается стартовая комбинация

        switch (mask[ii])                        //Например для nnllh будет 00aaA
        {
        case 'l': buff[ii] = 'a'; break;
        case 'h': buff[ii] = 'A'; break;
        case 'n': buff[ii] = '0'; break;
            default:
                break;
        }
    }
    ii++;
    buff[ii] = '\0';                            //Добавляем маркер конца строки
    double flagc = quant / 10;                  //Константа для поиска процента завершения
    double flag = flagc;                        //Переменная процента завершения
    int per = 1;                                //Множитель процента
    for ( ii = 0; ii < quant; ii++) {                                   //Основной цикл
        out << buff << endl;                                            //Сохраняем пароль в файл
        if (ii >= flag) {                        //Если программа завершила 10%
            cout << per * 10 << "%\n";           //Выводим проценты
            per++;
            flag += flagc;
        }
        for (int ii = len - 1; ii >= 0; ii--) {                        //начинаем посимвольный перебор с конца строки
            if (isMax(mask, i, buff) == 1) {                           //Если встречаем последний возможный символ в данной позиции, то меняем его на стартовый
                switch (mask[ii])
               {
                case 'l': if (buff[ii] == 'z')buff[ii] = 'a'; break;
                case 'h': if (buff[ii] == 'Z')buff[ii] = 'A'; break;
                case 'n': if (buff[ii] == '9')buff[ii] = '0'; break;
              default:
                    break;
                }
                continue;    //Переход в следующую итерацию цикла
            }
            buff[ii] +=1;     //Сама инкрементация пароля
            break;            //Конец внутреннего цикла
        }
}
    return 0;
}
int isMax(char mask[], int num, char in[]){
    switch (mask[num])
    {
case 'l': if (in[num] == 'z')return 1; else return 0;            //Если символ последний, то возвращаем "1", в противном случае "0"
    case 'h': if (in[num] == 'Z')return 1; else return 0;
    case 'n': if (in[num] == '9')return 1; else return 0;
    default:
        break;
    }
}
