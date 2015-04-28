#include<stdio.h>
void printpattern(int n)
{
int i,j,k;
for(i=0;i<n;i++)
{ for(k=n;k>i;k--)
{printf(" ");}
for(j=0;j<i;j++)
{printf("* ");}
printf("\n");
}
}
int main()
{
int n=20;
printpattern(n);
}