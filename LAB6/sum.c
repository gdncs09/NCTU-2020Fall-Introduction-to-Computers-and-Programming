#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int main(int argc, char *argv[]) //Command Line 標準
{
    int N=-1,total=0;
    int num[MAX]={0};

    for (int i=1; i<=argc;i++)//argc存有幾個分子
    {
        N++;
        num[N]=atoi(argv[i]);//Change string to integer;
    }

    for (int i=0;i<=N;i++) total+=num[i];//計算總數

    printf("Total: %d",total);
    return 0;
}
