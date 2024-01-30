#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool leap_year_jungle(int year);

int main()
{
          int year;
          printf("Input a year: ");
          scanf("%d",&year);

          if (leap_year_jungle(year)) //True
                    printf("%d is a leap year.\n",year);
          else
                    printf("%d is not a leap year.\n",year);
          return 0;
}

bool leap_year_jungle(int year)
{
          if (((year%100 == 0) && (year%400 ==0)) || ((year%100 != 0) && (year%4 == 0))) //Nếu chia hết cho 100 thì phải chia hết cho 400 (thế kỷ) hoặc không chia hết cho 100 và chia hết cho 4 (thập kỷ)
          {
                    return 1; //True
          }
          else return 0; //False
}
