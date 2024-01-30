#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

void BubbleSort(int *target, int N);

int main()
{

          int N;
          printf("Enter the size of the array: ");
          scanf("%d",&N); //Input N

          int arr[MAX];
          int *p;
          printf("Enter the numbers of src: ");
          for (p = &arr[0]; p < &arr[N]; p++) //Input Pointer từ 0 đến N-1
          {
                    scanf("%d",p);
          }
          p = &arr[0];
          BubbleSort(p,N); //Sort
          printf("target: ");
          for (p = &arr[0]; p < &arr[N]; p++) //Output value từ 0 đến N-1
          {
                    printf("%d ",*p);
          }
    return 0;
}

void BubbleSort(int *p, int N)
{
          for (int i = 1; i <= N; i++)
          {
                    for (int j = 0; j < N-1; j++)
                    {
                               if  (*(p+j) > *(p+j+1)) //Giá trị trước lớn hơn giá trị sau
                              { //swap
                                        int tmp = *(p+j);
                                        *(p+j) = *(p+j+1);
                                        *(p+j+1) = tmp;
                              }
                    }
          }
}

