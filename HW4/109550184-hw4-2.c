#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define NUM_LETTERS 26

void read_word(int count[NUM_LETTERS]);
bool equal_arr(int count1[NUM_LETTERS],int count2[NUM_LETTERS]);

int main()
{
          int count1[NUM_LETTERS] = {0};
          int count2[NUM_LETTERS] = {0};
          printf("Enter first word: ");
          read_word(count1);
          printf("Enter second word: ");
          read_word(count2);

          if (equal_arr(count1,count2))
                    printf("The words are anagrams.\n");
          else
                    printf("The words are not anagrams.\n");
          return 0;
}

void read_word(int count[NUM_LETTERS])
{
          char ch;
          do
          {
                    scanf("%c",&ch);
                    if (isalpha(ch))
                    {
                              ch = tolower(ch);
                              count[ch-97]++;
                    }
          } while (ch != '\n');
}

bool equal_arr(int count1[NUM_LETTERS],int count2[NUM_LETTERS])
{
          for (int i = 0; i < NUM_LETTERS; i++)
          {
                    if (count1[i] != count2[i])
                              return 0;
          }
          return 1;
}
