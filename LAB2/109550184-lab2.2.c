#include <stdio.h>
#include <stdlib.h>

int main()
{
          int money, m20 = 0, m10 = 0, m5 = 0, m1 = 0;
          printf("Enter a dollar amount: ");
          scanf("%d",&money);

          m20 = money / 20;
          money -= m20*20;

          m10 = money / 10;
          money -= m10*10;

          m5 = money / 5;
          money -= m5*5;

          m1 = money;

          printf("$20 bills: %d\n",m20);
          printf("$10 bills: %d\n",m10);
          printf("$5 bills: %d\n",m5);
          printf("$1 bills: %d\n",m1);
          return 0;
}
