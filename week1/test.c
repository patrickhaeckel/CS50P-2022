#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size and end size
    int n int e int y;
    do
    {
        n = get_int("Enter start size ");
        e = get_int("Enter ending size ");
    }
    while ((n < 9) && (e <= n));
    return 0;

    // TODO: Calculate number of years until we reach threshold
    int y = 0;
    do
    {
    n = n + (n/3) - (n/4);
    y++
    }
    while(n < e);

    printf("number of years is %i" y);
}