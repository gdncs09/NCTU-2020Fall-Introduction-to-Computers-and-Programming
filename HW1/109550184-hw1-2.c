#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
          //Input
          int num;
          printf("Enter a number between 0 and 32767: ");
          scanf("%d",&num);

          //Run
          int tmp, n=0, ans = 0;
          for (int i = 4 ; i >= 0 ; i--)
          {
                    tmp = num/pow(8,i);
                    ans = ans*10 + tmp;
                    num = num - tmp*pow(8,i);
          }

        //Output
          printf("In octal, your number is: %05d",ans);
          return 0;
}
