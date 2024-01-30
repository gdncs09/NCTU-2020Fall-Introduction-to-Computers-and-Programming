#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int main()
{
          int num, n = -1;
          int a[MAX];
          int *arr;
          char ch;
          printf("Input: ");
          do
          {
                    n++;
                    scanf("%d%c",&a[n],&ch);
          } while (ch != '\n');

          arr = &a[0];
          SelectionSort(arr,n);

          printf("Output: ");
          for (int i = 0; i <= n; i++)
          {
                    printf("%d ",a[i]);
          }
          return 0;
}

void SelectionSort(int *arr, int n)
{
          for (int i  = 0; i < n; i++)
          {
                    int min = i; //mặc định giá trị ở vị trí thứ i là MIN
                    for (int j = i+1; j <= n; j++)
                    {
                              if (*(arr+min) > *(arr+j)) //giá trị ở vị trí min > giá trị ở vị trí thứ j
                              {
                                        min = j; //cập nhật vị trí min
                              }
                              //swap
                              int tmp = *(arr+i);
                              *(arr+i) = *(arr+min);
                              *(arr+min) = tmp;
                    }
          }
}
