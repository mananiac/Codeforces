/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <conio.h>
using namespace std;
int main()
{int n,a,c,k,x;
char b[150];
cin>>n;
x=0;
for(a=0;a<n;a++)
{
    cin>>b;


    for(c=0;b[c]!='\0';c++)
    {
        if(b[c]=='+' && b[c+1]=='+')
        {
            x=x+1;
        }
        else if(b[c]=='-' && b[c+1]=='-')
        {
            x=x-1;
        }
        else
        {
        continue;
        }
    }
}
cout<<x;
}
