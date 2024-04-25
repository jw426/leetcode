/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(int* n1, int* n2);
int binary_search(int lo, int hi, int* nums, int target, int find_start);
int* make_range_array(int start, int end, int* returnSize);

int* searchRange(int* nums, int numsSize, int target, int* returnSize) {

    int i_start = binary_search(0, numsSize, nums, target, 1);
    int i_end = binary_search(0, numsSize, nums, target, 0);
    return make_range_array(i_start, i_end, returnSize);
}

int* make_range_array(int start, int end, int* returnSize) {

    int* ran_arr =  (int*)malloc(sizeof(int)*2);
    *returnSize = 2;

    if (start >= end) {
        ran_arr[0] = -1;
        ran_arr[1] = -1; 
    }
    else {
        ran_arr[0] = start;
        ran_arr[1] = end - 1;
    }

    return ran_arr;   
}

int binary_search(int lo, int hi, int* nums, int target, int find_start) {
    
    int mid = (lo + hi) / 2;
    if (lo >= hi) return mid;  

    int outcome; 
    // target <= comparison key
    if ((outcome = cmp(&target, nums+mid)) < 0) {
        return binary_search(lo, mid, nums, target, find_start);
    // target >  comparison key
    } else if (outcome > 0) {
        return binary_search(mid + 1, hi, nums, target, find_start);
    } else {
        if (find_start) return binary_search(lo, mid, nums, target, find_start);
        return binary_search(mid + 1, hi, nums, target, find_start);
    }
}

int cmp(int* n1, int* n2) {
    return *n1 - *n2; 
}