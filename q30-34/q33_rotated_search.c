int search(int* nums, int numsSize, int target) {
    
    if (numsSize <= 0) return -1;

    int i; 
    int low = 0, high = numsSize;
    while (low < high) {
        i = (low + high) / 2;
        if (target < nums[i]) {
            printf("inside first %d, %d, %d\n", nums[i], nums[low], nums[high-1]);
            if (nums[i] < nums[high-1]) high = i; 
            else if (nums[i] > nums[high -1]) {
                if (nums[high-1] >= target) low = i + 1;
                else high = i; 
            } else high = i;
        } else if (nums[i] < target) {
            printf("inside second %d, %d, %d\n", nums[i], nums[low], nums[high-1]);
            if (nums[low] < nums[i]) low = i; 
            else if (nums[low] > nums[i]) {
                if (target < nums[low]) low = i + 1;
                else high = i;
            } else low = i + 1;
        } else return i;
    }
    return -1;
}