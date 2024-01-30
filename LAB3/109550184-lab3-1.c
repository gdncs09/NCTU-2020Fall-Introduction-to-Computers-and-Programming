#include <stdio.h>
#include <stdlib.h>
#define MAX 26

void FillArr(int a[MAX])
{
          for (int i = 0; i < MAX; i++)
                    a[i] = 0;
}

int main()
{
          int count[MAX];
          char ch;
          FillArr(count);
          printf("Enter a word (LOWER-CASE): ");
          do
          {
                    scanf("%c",&ch);
                    count[ch-97]++; //Đếm kí tự
          } while (ch != '\n');

          printf("The distinct alphabets\n");
          for (int i = 0; i < MAX; i++)
          {
                    if (count[i] !=0) //Nếu như tồn tại kí tự i+97
                              printf("%c: %d\n",i+97,count[i]);
          }
          return 0;
}
