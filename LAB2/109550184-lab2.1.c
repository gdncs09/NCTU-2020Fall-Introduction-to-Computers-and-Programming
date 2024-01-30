#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
         char phone[15],ans[15];
         int n=-1;
          printf("Enter phone number [(xxx) xxx-xxxx]: ");
          gets(phone);

          for (int i = 1; i < strlen(phone); i++)
          {

                    if  (phone[i] >= '0' && phone[i] <= '9') //如果phone[i]是號碼就不換
                    {
                              n++;
                              ans[n]=phone[i];
                    }
                    else
                    {
                              if (phone[i] != ' ')
                              {
                                        n++;
                              }

                              ans[n] = '.';
                    }
          }

          printf("You entered: %s",ans);
          return 0;
}
