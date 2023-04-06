#include <stdio.h>
#include <stdlib.h>

int main()
{
          int m1,d1,y1,m2,d2,y2;
          char tmp;
          printf("Enter first date (mm/dd/yy): ");
          scanf("%d%c%d%c%d",&m1,&tmp,&d1,&tmp,&y1); //輸入 month,day,year

          printf("Enter second date (mm/dd/yy): ");
          scanf("%d%c%d%c%d",&m2,&tmp,&d2,&tmp,&y2);


          if (y1 > y2 || (y1 == y2 && m1 > m2) || (y1==y2 && m1 == m2 && d1 > d2)) //符合date1 > date2 的條件 檢查1.year - 2.month - 3.day
          {
                    printf("%d/%d/%02d comes after than %d/%d/%02d",m1,d1,y1,m2,d2,y2);
          }
          else if (y1 < y2 || (y1 == y2 && m1 < m2) || (y1==y2 && m1 == m2 && d1 < d2)) //date1 <date2
          {
                    printf("%d/%d/%02d comes after than %d/%d/%02d",m2,d2,y2,m1,d1,y1);
          }
          else //date1 = date2
          {
                    printf("-1");
          }
          return 0;
}
