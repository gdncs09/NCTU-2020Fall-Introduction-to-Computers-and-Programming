#include <stdio.h>
#include <stdlib.h>

int main()
{
          //Input
          int num;
          printf("Enter a two-digit number: ");
          scanf("%d",&num);

          //Run
          int ans = 0;
          while (num != 0)
          {
                    ans = ans*10 + num%10;
                    num /= 10;
          }

          //Output
          printf("The reversal is: %d",ans);
          return 0;
}
