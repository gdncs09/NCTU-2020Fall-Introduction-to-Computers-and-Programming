#include <stdio.h>
#include <stdlib.h>

int GCD(int a, int b);
void reduce(int numerator, int denominator, int *reduce_numerator, int *reduce_denominator);

int main()
{
          int numerator, denominator;
          float value;
          printf("Enter a fraction: ");
          scanf("%d/%d",&numerator,&denominator);

          reduce(numerator,denominator,&numerator,&denominator); //lowest terms
          value = numerator / (float)denominator;//ép kiểu (số nguyên / số nguyên = số nguyên, tuy nhiên 1 hoặc 2 là số thực kq = số thực)

          printf("In lowest terms: %d/%d",numerator,denominator);
          printf("\nThe value is: %.01f",value); //Lấy 1 số sau dấu chấm
          return 0;
}

int GCD(int a, int b) //Euclid
{
          if (b == 0)
          {
                    return a;
          }
          else
          {
                    GCD(b,a%b);
          }
}

void reduce(int numerator, int denominator,int *reduce_numerator,int *reduce_denominator)
{
          int m;
          m = GCD(numerator, denominator); //UCLN
          *reduce_numerator /= m;
          *reduce_denominator /= m;
}
