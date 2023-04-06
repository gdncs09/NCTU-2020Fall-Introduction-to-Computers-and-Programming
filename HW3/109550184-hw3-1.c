#include <stdio.h>
#include <stdlib.h>
#define N 8

void bubblesort(int a[N])
{
          int tmp;
          for (int i = 0; i < N; i++)
          {
                    for (int j = 0; j < N; j++)
                    {
                              if (a[j] > a[j+1]) //前比後大
                              {
                                        tmp = a[j]; //swap
                                        a[j] = a[j+1];
                                        a[j+1] = tmp;
                              }
                    }
          }
}

int main()
{
          int a[N];
          printf("Enter 8 number: ");
          for (int i = 0; i < N; i++) //Input
          {
                    scanf("%d",&a[i]);
          }

          bubblesort(a);
          printf("Answer: ");
          for (int i = 0; i < N; i++) //Output
          {
                    printf("%d ",a[i]);
          }
          return 0;
}
