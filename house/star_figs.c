#include <stdio.h>

void topleft(int h);
void bottomleft(int h);
void bottomright(int h);
void topright(int h);

int main(void)
{
    topleft(5);
    bottomleft(5);
    bottomright(5);
    topright(5);
}

void topleft(int h)
{
    if (h<=0)
    {
        return;
    }

    for (int i = 0; i < h; i++)
    {
        printf("*");
    }
    printf("\n");

    topleft(h-1);

}

void bottomleft(int h)
{
    if (h<=0)
    {
        return;
    }

    bottomleft(h-1);

    for (int i = 0; i < h; i++)
    {
        printf("*");
    }
    printf("\n");
}

void bottomright(int h)
{
    for (int i = 0; i < h; i++)
    {
        for (int k = 0 ; k < h - i - 1; k++)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}

void topright(int h)
{
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf(" ");
        }
        for (int k = 0 ; k < h - i; k++)
        {
            printf("*");
        }
        printf("\n");
    }
}