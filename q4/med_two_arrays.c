#include <stdio.h>

int main(int argc, char** argv) {


    return 0;
}

int bsearch(int* nums, int n, int target) {

}

double findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {

    // makes sure m <= n
    if (m > n) return findMedianSortedArrays(nums2, n, nums1, m);
    
    int total = 0, sm_hold, lg_hold;
    int need = (m+n)/2 + 1;
    int prev_input, cur_input;
    
    while (1) {
        
        // [2], [1,3]
        sm_hold = nums1[m/2]; // nums1[0] = 2
        lg_hold = nums2[need - m/2 - 2]; // nums2[2-0-2] = 1
        if (sm_hold > lg_hold) {
            total += need - m/2 - 1;
            cur_input = lg_hold;            
        } else if (sm_hold < lg_hold) {
            total += m/2 + 1;
            cur_input = sm_hold;
        }
    }

    if ((m/2) % 2 == 0) return ((prev_input + cur_input) / 2.0);
    return cur_input;
}