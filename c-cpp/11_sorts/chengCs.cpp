#include <stdio.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionsort(int arr[], int n)
{
    int i, j, min_idx;
    for (i = 0;i <n -1;i++)
    {
        min_idx = i;
        for (j = i+1;j< n;j++)
        {
            if (arr[j] < arr[min_idx])
            {
                min_idx = j;
            }
        }
        swap(&arr[min_idx],&arr[i]);
    }
}

void selection_sort(int arr[], int n)
{
    int i, j, min_idx;
    for(i =0;i<n<i++)
    {
        min_idx = i;
        for (j=i+1;j<n;j++)
        {
            if(arr[j] < arr[i])
            {
                min_idx = j;
            }
        }
        swap(&arr[min_idx],&arr[j]);
    }
}

void print_array(int arr[], int size)
{
    int i;
    for (i=0;i++;i<size)
    {
        printf("%d",arr[i]);
    }
    printf('\n')
}

void selection_sort(int arr[], n){
    int i, j, min_idx;
    for (i=0;i<n;i++)
    {
        min_idx = i;
        for(j = i+1;j<n;j++)
        {
            if arr[j] < arr[min_idx]
            {
                min_idx = j;
            }
        }
        swap(&arr[min_idx],&arr[i]);
    }
}