#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;
    int x;
    int i;
    int y;
    // to restrict intput to be between 1 & 8 inclusive
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    // beginning of the loop to make the tower
    for (i = 0; i < h;)
    {
        // to make the tower right aligned
        for (y = 0; y < h - i - 1;)
        {
            printf(" ");
            y = y + 1;
        }
        // prints the actual tower with hastags
        printf("#");
        for (x = 0; x < i;)
        {
            printf("#");
            x = x + 1;
        }
        i = i + 1;
        printf("\n");
    }
}