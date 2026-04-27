#include <stdio.h>
#include <conio.h>
void main()
{
    int arr[100], i, size, max, min;
    clrscr();
    printf("Enter number of values\n");
    scanf("%d", &size);

    for(i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }
    max = arr[0];
    for(i = 0; i < size; i++)
    {
        if(arr[i] > max)
        {
            max = arr[i];
        }
    }
    min = arr[0];
    for(i = 0; i < size; i++)
    {
        if(arr[i] < min)
        {
            min = arr[i];
        }
    }
    printf("Maximum value in array = %d\n", max);
    printf("Minimum value in array = %d\n", min);
    getch();
}