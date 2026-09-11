#include <stdio.h>
#include <stdlib.h>

// int get_positive_int(void);
void space(int h, int i);
void star(int i);
void star_(int i);
void roof(int height);
void line_spaces(int n);
void line_stars(int n);
void mid(int height); 
void windows(int height);
void doors(int height);
void baseline(int height);
void window_struct(int height, int deduction);

int main(int argc, char argv[])
{
    // int height = get_positive_int();
    if (argc == 1 || argc > 2)
    {
        printf("Usage: ./house size.\n");
        return 1;
    }
    else
    {
        int height = atoi(argv[1]);
        if (height < 6)
        {
            printf("Size too less!\n");
            return 2;
        }
        roof(height);
        mid(height);
        windows(height);
        mid(height);
        doors(height);
        baseline(height);
        printf("\n");
        printf("\n");
    }
}


// int get_positive_int(void)
// {
//     int n;
//     do
//     {
//         printf("Size?: ");
//         scanf("%d", &n);
//     }
//     while (n<0);
//     return n;
// }

void space(int h, int i)
{
    for (int j=0; j<h-i-1;j++)
    {
        printf("  ");
    }
}

void star(int i)
{
    for (int m=0; m<i; m++)
    {
        printf(" *");
    }
}

void star_(int i)
{
    for (int m=0; m<i; m++)
    {
        printf("* ");
    }
}

void roof(int height)
{
    line_spaces(2*height-2);
    line_stars(1);
    for (int i=0; i<height; i++)
    {
        space(height, i);
        star(i);
        printf(" ");
        star_(i);
        space(height, i);
        printf("\n");
    }
}

void line_stars(int n)
{
    for (int i = 0; i<n; i++)
    {
        printf("*");
    }
}

void line_spaces(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}

void mid(int height)
{
    for (int i = 0; i < height/3; i++)
    {
        line_spaces(1);
        line_stars(1);
        line_spaces(4*height-7);
        line_stars(1);
        printf("\n");
    }
}

void windows(int height)
{
    if (height%2 == 0)
    {
        window_struct(height, 7);
    }
    else
    {
        window_struct(height, 5);
    }
}

void window_struct(int height, int deduction)
{
    for (int i = 0; i < height/3; i++)
    {
        line_spaces(1);
        line_stars(1);

        line_spaces(height/2);
        line_stars(height/2);
        
        line_spaces(2*height-deduction);

        line_stars(height/2);
        line_spaces(height/2);
        line_stars(1);
        printf("\n");
    }
}

void doors(int height)
{
    line_spaces(1);
    line_stars(1);
    line_spaces(height);
    line_stars(2*height - 7);
    line_spaces(height);
    line_stars(1);
    printf("\n");
    for (int i = 0; i < (3*height)/5; i++)
    {
        line_spaces(1);
        line_stars(1);
        line_spaces(height);
        line_stars(1);
        line_spaces(2*height-9);
        line_stars(1);
        line_spaces(height);
        line_stars(1);
        printf("\n");
    }
}


void baseline(int height)
{
    for (int i = 0; i <(2*height)-2; i++)
    {
        printf(" *");
    }
}


