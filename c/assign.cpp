//применение арифметических операций с присваиванием
#include <iostream> /* Библиотека (стандарт) */
#include <locale.h> /* Русификатор */

using namespace std;
int main()
{
int ans = 27;
ans += 10; //то же самое, что и ans = ans +10;
cout << ans << ".";


ans -= 7; //то же самое, что и ans = ans -7;
cout << ans << ".";

ans *= 2; //то же самое, что и ans = ans *2;
cout << ans << ".";

ans /= 3; //то же самое, что и ans = ans /3;
cout << ans << ".";

ans %= 3; //то же самое, что и ans = ans %3;
cout << ans << ".";

return 0;
}

