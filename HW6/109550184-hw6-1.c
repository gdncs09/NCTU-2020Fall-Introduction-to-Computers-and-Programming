#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 256

int main()
{
          char length_word[MAX],word[MAX];
          int count = 0;
          do
          {
                    printf("Enter word: ");
                    scanf("%s",word);
                    count++;
                    if (count == 1) //First word
                              strcpy(length_word,word); //Because length_word == NULL
                    if (strcmp(length_word,word) < 0) //length_word < word
                              strcpy(length_word,word); //length_word = word
          } while (strlen(word) != 3); //Enters a three-letter word > stop
          printf("The largest word is %s",length_word);
          return 0;
}
/*
Write a program that finds the largest words (no longer than 20 characters).
The program will determine which word would come first and last in dictionary
order. The program stops accepting input when the user enters a three-letter
word.
Input:
Enter word: zero
Enter word: zebra
Enter word: catfish
Enter word: cat
Output:
The largest word is zero.
Hint : Use a string name largest_word to keep track of the largest word.
Each time the user enters a new word, use strcmp to compare it with
largest_word ; if the new word is larger, use strcpy to save it in
largest_word . Use strlen to determine when the user has entered a
three-letter word.
*/


