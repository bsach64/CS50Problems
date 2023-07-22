#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // This program says hello to you
    string name = get_string("What's your name?");
    printf("hello, %s\n", name);
}