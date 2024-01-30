#include <stdio.h>
#include <stdlib.h>
#define N 5

void FillArr(int a[N])
{
          for (int i = 0; i < N; i++)
                    a[i] = 0;
}

void Input(int i, int row[N],int column[N])
{
          int a;
          printf("Enter row %d: ",i+1);
          for (int j = 0; j < N; j++)
          {
                    scanf("%d",&a);
                    row[i]+=a; //Cộng dồn Dòng thứ .....
                    column[j]+=a; //Cộng dồn Cột thứ .....
          }
}

int main()
{
          int row[N],column[N];
          FillArr(row);
          FillArr(column);
          for (int i = 0; i < N; i++)
                    Input(i,row,column); //Nhập dòng thứ ....

          printf("Row totals: ");
          for (int i = 0; i < N; i++)
                    printf("%d ",row[i]);
          printf("\nColumn totals: ");
          for (int i = 0; i < N; i++)
                    printf("%d ",column[i]);
          return 0;
}
