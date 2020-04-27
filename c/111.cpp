#include <iostream>
using namespace std;
int main()
{
//std::string readAll(const std::string &fileName);
//...
//using namespace EasyGumbo;

//jauto page = readAll(argv[1]);
//Gumbo parser(&page[0]);
//
//
//
//int s = 0, n = 20;
//while (s+n<=100) {
//	s=s+25;
//	n=n-5;
//}
//cout<<s;
int N=9;
int s=0;
//int i;
//int A[i];
//int A[N];

for(int i=0;i<=N;++i) {
	if (int A[i]<A[N]) {
		++A[i];
		--A[N];
		++s;
	}
cout<<s;
}
return 0;
}
