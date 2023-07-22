#include <stdio.h>
#include <cs50.h>

int digit_count(long number);

int main(void)
{
    long input = get_long("Number: ");
    long credit_number = input;
    int odd_sum = 0;
    do
    {
        int two_digit;
        two_digit = credit_number % 100;
        int one_digit;
        one_digit = credit_number % 10;
        credit_number = (credit_number - two_digit) / 100;
        two_digit = (two_digit - one_digit) / 10;
        two_digit = two_digit * 2;
        do
        {
            int two_digit_reminder = two_digit % 10;
            odd_sum = odd_sum + two_digit_reminder;
            two_digit = two_digit / 10;
        }
        while (two_digit != 0);
    }
    while (credit_number != 0);

    int even_sum = 0;
    long evens_number = input;
    do
    {
        int ones_place;
        int tens_place;
        tens_place = evens_number % 100;
        ones_place = tens_place % 10;
        even_sum = even_sum + ones_place;
        evens_number = (evens_number - tens_place) / 100;
    }
    while (evens_number != 0);

    int count = digit_count(input);
    int sum = even_sum + odd_sum;

    long check = input;
    do
    {
        int rem = check % 10;
        check = (check - rem) / 10;
    }
    while (check > 100);

    if (sum % 10 == 0)
    {
        if (check == 34 || check == 37)
        {
            if (count == 15)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (check == 51 || check == 52 || check == 53 || check == 54 || check == 55)
        {
            if (count == 16)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            int rem_v = check % 10;
            int x = (check - rem_v) / 10;
            if (x == 4)
            {
                if (count == 13 || count == 16)
                {
                    printf("VISA\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
            else
            {
                printf("INVALID\n");
            }
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int digit_count(long number)
{
    int count = 0;
    do
    {
        int rem = number % 10;
        number = (number - rem) / 10;
        count = count + 1;
    }
    while (number > 0);
    return count;
}