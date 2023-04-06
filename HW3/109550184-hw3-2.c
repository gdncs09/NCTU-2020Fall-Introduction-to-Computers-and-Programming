#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define MAX 26

void Input(int a[MAX])
{
          int ch;
           do
          {
                    scanf("%c",&ch);
                    if (isalpha(ch)) //Nếu là chữ
                    {
                              ch = tolower(ch); //Chữ thường
                              a[ch-97]++; // Đếm có bao nhiêu lần xuất hiện kí tự ch

                    }
          } while (ch != '\n');
          return a;
}

void FillArr(int a[MAX])
{
          for (int i = 0; i < MAX; i++)
                    a[i] = 0;
}
int main()
{
          int a[MAX],b[MAX];
          FillArr(a);
          FillArr(b);
          int result = 1;
          printf("Enter first word: ");
          Input(a);
          printf("Enter second word: ");
          Input(b);

          for (int i = 0; i < MAX; i++)
          {
                    if (a[i] != b[i]) //Nếu số lượng kí tự không bằng nhau
                    {
                              result = 0;
                              break;
                    }
          }
          if (result) //True result = 1
          {
                    printf("The words are anagrams.");
          } else //result = 0
          {
                    printf("The words are not anagrams.");
          }
          return 0;
}
