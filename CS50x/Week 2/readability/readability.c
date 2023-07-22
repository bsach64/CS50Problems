#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Gets the text from the user
    string text = get_string("Text: ");

    // Counts the number of letters in the text
    int letters = count_letters(text);

    // Counts the number of words in the text
    int words = count_words(text);

    // Counts the number of sentences in the text
    int sentences = count_sentences(text);

    // Calculates L & S
    float L = (letters / (float) words) * 100;
    float S = (sentences / (float) words) * 100;

    // Calculates the index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Rounds the index to give a grade
    int grade;
    if (index - (int) index > 0.5)
    {
        grade = (int) index + 1;
    }
    else
    {
        grade = (int) index;
    }

    // prints the grade
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }

}

// Function to count letters in a body of text

int count_letters(string text)
{
    int nol;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            nol = nol + 1;
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            nol = nol + 1;
        }
    }
    printf("Letters: %i\n", nol);
    return nol;
}

// Function to count words in a body of text

int count_words(string text)
{
    int now = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == 32)
        {
            now = now + 1;
        }
    }
    printf("Words: %i\n", now);
    return now;
}

// Function to count sentences in a body of text

int count_sentences(string text)
{
    int nos = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == 33)
        {
            nos = nos + 1;
        }
        else if (text[i] == 46)
        {
            nos = nos + 1;
        }
        else if (text[i] == 63)
        {
            nos = nos + 1;
        }
    }
    printf("Sentences: %i\n", nos);
    return nos;
}