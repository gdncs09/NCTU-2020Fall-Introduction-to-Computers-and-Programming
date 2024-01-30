#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX 100

float answer(float x[MAX],int n);

int main()
{
          int n=-1;
          char ch;
          float x[MAX];
          char a[100];
          //Input
          printf("Enter a row: ");
          do
          {
                    //Run
                    n++;
                    scanf("%f%c",&x[n],&ch); //ch để giải quyết '\n'
          } while (ch != '\n');

          //Output
          printf("%.02f",answer(x,n)); //Lấy 2 số sau dấu chấm
          return 0;
}

float answer(float x[MAX],int n)
{
        float ans = 0;
        for (int i = 0; i <= n; i++)
            ans+=pow(x[i],2); //bình phương
        return ans;

}
