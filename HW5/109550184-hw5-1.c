#include <stdio.h>
#include <stdlib.h>

#define N 6

int main()
{
          int arr[N];
          int *p;
          printf("array = ");
          for (p = &arr[0]; p < &arr[N]; p++) //Chạy xuôi từ 0 đến N-1
          {
                    scanf("%d",p); //Input pointer
          }

          printf("reserve_array = ");
          for (p = &arr[N-1]; p >= &arr[0]; p--) //Chạy ngược từ N-1 về 0
          {
                    printf("%d ",*p); //Output value
          }
          printf("\n%d",sizeof(p));
          printf("\n%d",sizeof(*p));
          printf("\n%d",sizeof(arr));
          return 0;
}
