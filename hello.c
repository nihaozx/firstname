#include<stdio.h>
#include <string.h>
#include <stdbool.h>


int *removeElement(int* nums, int numsSize, int val)
{
    int temp = 0;
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i] != val)
        {
            nums[temp] = nums[i];
            temp++;
        }
        
    }
   
    printf("temp = %d\n",temp);
    // for(int i=0;i<nums[temp];i++)
    // {
    //     printf("%d\t",nums[i]);
    // }
    return nums;

}

int main(void)
{
    int nums[]={3,2,2,3};
    int numsSize = sizeof(nums)/sizeof(int);
    int *p = removeElement(nums,numsSize,2);

    for(int i=0;i<sizeof(p)/sizeof(int);i++)
    {
        printf("%d\t",p[1]);
    }
    
    return nums;

    return 0;
}