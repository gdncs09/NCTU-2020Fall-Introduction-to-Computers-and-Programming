#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX 256
#define ABC 25

void FillArr(int face_value[ABC]);
int compute_scrabble_value(char *word, int N,int face_value[ABC]);

int main()
{
          char W[MAX];
          printf("Enter a word: ");
          scanf("%s",W);
          //int  face_value[ABC]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};//1:AEILNORSTU, 2:DG, 3:BCMP, 4:FHVWY, 5:K, 8:JX, 10:QZ.
          int face_value[ABC];
          FillArr(face_value);
          printf("Scrabble value: %d",compute_scrabble_value(&W[0],strlen(W),face_value));
          return 0;
}

void FillArr(int face_value[ABC])
{
          char str[MAX];
          for (int point=1; point<=10; point++)
          {
                    if (point==6 || point==7|| point==9) continue;
                    if (point==1) strcpy(str,"AEILNORSTU");
                    else if (point==2) strcpy(str,"DG");
                    else if (point==3) strcpy(str,"BCMP");
                    else if (point==4) strcpy(str,"FHVWY");
                    else if (point==5) strcpy(str,"K");
                    else if (point==8) strcpy(str,"JX");
                    else if (point==10) strcpy(str,"QZ");

                    for (int i=0; i<strlen(str); i++)
                    {
                    face_value[(int)str[i]-65]=point;
                    }
          }
}
int compute_scrabble_value(char *word, int N, int face_value[ABC])
{
          int sum = 0;
          for (int i = 0; i < N; i++)
          {
                    sum+=face_value[toupper(*(word+i))-65]; //ASCII [A..Z]=[65..90]
          }
          return sum;
}

/*
In the SCRABBLE Crossword Game, players form words using small tiles,
each containing a letter and a face value. The face value varies from one
letter to another, based on the letter¡¦s rarity. (Here are the face values:
1:AEILNORSTU, 2:DG, 3:BCMP, 4:FHVWY, 5:K, 8:JX, 10:QZ.)
Write a program that must include the following function:
int compute_scrabble_value(const char *word);
The function compute_scrabble_value will return the value of a word by
summing the values of its letters. The parameter char *word points to the
string entered by the user:
Enter a word: pitfall
Scrabble value: 12
Your program should allow any mixture of lower-case and upper-case letters
in the word.
*/
