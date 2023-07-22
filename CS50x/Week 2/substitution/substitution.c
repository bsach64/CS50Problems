#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    char lower_alphabet[26];
    for (int i = 0; i < 26; i++)
    {
        lower_alphabet[i] = 97 + i;
    }
    char upper_alphabet[26];
    for (int j = 0; j < 26; j++)
    {
        upper_alphabet[j] = 65 + j;
    }
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    if (strlen(argv[1]) != 26)
    {
        printf("26 alphabets to be entered\n");
        return 1;
    }
    int numbers[26];
    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if (argv[1][j] >= 97 && argv[1][j] <= 122)
            {
                if (argv[1][j] == 97 + i)
                {
                    numbers[i] = i;
                }
            }
            else if (argv[1][j] >= 65 && argv[1][j] <= 90)
            {
                if (argv[1][j] == 65 + i)
                {
                    numbers[i] = i;
                }
            }
        }
    }
    int flag = 1;
    for (int j = 0; j < 26; j++)
    {
        if (numbers[j] == j)
        {
            flag = flag * 1;
        }
        else
        {
            flag = flag * 0;
        }
    }
    if (flag == 1)
    {
        string plaintext = get_string("Plaintext: ");
        char cipher_lower[26];
        char cipher_upper[26];
        char cipher_text[strlen(plaintext)];
        for (int i = 0; i < 26; i++)
        {
            if (argv[1][i] >= 97 && argv[1][i] <= 122)
            {
                cipher_lower[i] = argv[1][i];
            }
            else if (argv[1][i] >= 65 && argv[1][i] <= 90)
            {
                cipher_lower[i] = tolower(argv[1][i]);
            }
        }
        for (int i = 0; i < 26; i++)
        {
            if (argv[1][i] >= 97 && argv[1][i] <= 122)
            {
                cipher_upper[i] = toupper(argv[1][i]);
            }
            else if (argv[1][i] >= 65 && argv[1][i] <= 90)
            {
                cipher_upper[i] = argv[1][i];
            }
        }
        for (int j = 0; j < strlen(plaintext) + 1; j++)
        {
            for (int i = 0; i < 26; i++)
            {
                if (plaintext[j] >= 97 && plaintext[j] <= 122)
                {
                    if (plaintext[j] - 97 == i)
                    {
                        cipher_text[j] = cipher_lower[i];
                    }
                }
                else if (plaintext[j] >= 65 && plaintext[j] <= 90)
                {
                    if (plaintext[j] - 65 == i)
                    {
                        cipher_text[j] = cipher_upper[i];
                    }
                }
                else
                {
                    cipher_text[j] = plaintext[j];
                }
            }
        }
        printf("ciphertext: %s", cipher_text);
        printf("\n");
        return 0;
    }
    else
    {
        printf("Not All Alphabets are Represented\n");
        return 1;
    }

    /*
    define an array of alphabets [both lower & upper case]
    if (no cmd line arguments are given)
        print error
    if (26 characters are not given)
        print error
    if (non alphabetic characters are given)
        print error
    check whether each alphabet is present
        use a flag value & for loop to check whether each alphabet is present
            if (not)
                print error
    get input (plaintext) from user
    match cipher[array] with plaintext[array]
    print cipher[array]
    */
}