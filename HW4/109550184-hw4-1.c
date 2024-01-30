#include <stdio.h>
#include <stdlib.h>

int Fibonacci(int n)
{
          if (n==1)
                    return 0;
          if (n==2)
                    return 1;
          return(Fibonacci(n-2)+Fibonacci(n-1)); //công thức tính fibonacci theo đệ quy
}

int main()
{
          int n;
          printf("Enter a number: "); //Input
          scanf("%d",&n);

          for (int i = 1; i <= n ; i++) printf("%d ",Fibonacci(i)); //Output
          return 0;
}




