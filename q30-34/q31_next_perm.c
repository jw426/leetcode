void nextPermutation(int* nums, int numsSize) {
    
    // only one case of permutation
    if (numsSize == 1) return; 

    int r = numsSize - 1; 
    int l = numsSize - 2; 
    while (l >= 0) { 

        // find right switch
        while (l < r) {
            // switch position found 
            if (nums[l] < nums[r--]) {
                swap_int(nums + l, nums + (++r));
                reverse(nums + l + 1, numsSize - l - 1);
                return; 
            } 
        }

        // permute one level down  
        l--;
        r = numsSize - 1;
    }
    reverse(nums + l + 1, numsSize - l - 1);
}

void swap_int(int* a1, int* a2) {
    int tmp = *a1; 
    *a1 = *a2; 
    *a2 = tmp; 
}

void reverse(int* nums, int n) {

    int i = 0, j = n-1; 
    while (i < j) {
        swap_int(nums + i++, nums + j--);
    }
}
