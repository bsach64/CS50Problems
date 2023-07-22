#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(char i, int x);

int main(int argc, string argv[])
{
    // checks if number of command line arguments = 2
    if (argc == 2)
    {
        bool alpha;
        // checks if string contains only digits in character
        alpha = only_digits(argv[1]);
        if (alpha == true)
        {
            // encrypts the input by modifying each character using the rotate function
            string plaintext = get_string("Plaintext:  ");
            int cipher = atoi(argv[1]);
            printf("ciphertext: ");
            for (int i = 0, len = strlen(plaintext); i < len; i++)
            {
                char ct = rotate(plaintext[i], cipher);
                printf("%c", ct);
            }
            printf("\n");
            return 0;
        }
        else
            // prints error if string contains other than digits
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    // prints error if number of command line arguments > 2
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

// function checks if each character in a string is an array
bool only_digits(string s)
{
    bool onlydigits;
    int len = strlen(s);
    int TF[len];
    int product = 1;
    for (int i = 0; i < len; i++)
    {
        TF[i] = isdigit(s[i]);
        // using the output of the isdigit() function it calculates the product if the string contains an character the product = 0, thus is not a valid input
        product = product * TF[i];
    }
    if (product != 0)
    {
        onlydigits = true;
    }
    else
    {
        onlydigits = false;
    }
    return onlydigits;

}

// functions "rotates" each character as the user desires
char rotate(char i, int x)
{
    int o = 0;
    char c = '\0';
    // changes character when letter is not capitalized
    if (i >= 65 && i <= 90)
    {
        x = x % 26;
        o = i + x;
        if (o >= 65 && o <= 90)
        {
            c = o;
            return c;
        }
        else if (o > 90)
        {
            int y;
            int s;
            y = o - 90;
            s = 64 + y;
            return s;
        }
    }
    // changes character when letter is capitalized
    else if (i >= 97 && i <= 122)
    {
        x = x % 26;
        o = i + x;
        if (o >= 97 && o <= 122)
        {
            c = o;
            return c;
        }
        else if (o > 122)
        {
            int y;
            int s;
            y = o - 122;
            s = 96 + y;
            return s;
        }
    }
    else
    {
        c = i;
        return c;
    }
    return c;
}