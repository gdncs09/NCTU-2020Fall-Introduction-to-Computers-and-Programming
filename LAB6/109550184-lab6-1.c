#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h> //bool
#define MAX 101

bool check_id(char *id, int N);

int main()
{
          int N;
          char ID[MAX];
          char *id;
          printf("Enter an ID number: ");
          fgets(ID,MAX-1,stdin); //Input String from keyboard
          N = strlen(ID); //String Length Độ dài String
          id = &ID[0]; //pointer

          if (check_id(id,N)) //True
          {
                    printf("It is a correct ID number.");
          }
          else //False
          {
                    printf("It isn't a correct ID number.");
          }
          return 0;
}

bool check_id(char *id, int N)
{
          if ((int)*id < 65 || (int)*id > 90) //The first character [A..Z] = [65..90]
                    return false; //False
          if (*(id+1) != '1' && *(id+1) != '2') //The second character =1 or =2
                    return false; //False
          for (int i = 2; i < N; i++) //The others
          {
                    if (*(id+i) > '9') //Not digitals
                              return false; //False
          }
          return true; //True
}

/*
1. Write a program that determines whether it is a correct form of ID number.
Input:
Enter an ID number: A123456789
Output:
It is a correct ID number.
Input:
Enter an ID number: a323456789
Output:
It isn’t a correct ID number.
Hint: Use the following function which is used to check whether the form is correct:
bool check_id (char* ID);
The first character should be in upper case and the second character should be either
1 or 2, the others can be any digitals.
*/
