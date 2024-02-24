#include <math.h>
#include <limits.h>
#include <stdio.h>

#define DEBUG 1

void print_array(int* nums, int n) {
    for (int i = 0; i<n; i++) {
        printf(" %d ", nums[i]);
    }
    printf("\n");
}

double _findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {
    
    #if DEBUG
    printf("%d, %d\n", m, n);
    print_array(nums1, m);
    print_array(nums2, n);
    #endif
    if (m > n) _findMedianSortedArrays(nums2, n, nums1, m);

    int total_cnt = (m+n)/2; // need total_cnt elements in 
    int cur_cnt = 0; 
    while (cur_cnt < total_cnt) {
        
        int sm_idx = m/2; 
        int res_idx = total_cnt - cur_cnt - m/2 - 1;
        printf("%d, %d\n", sm_idx, res_idx);

        while (nums1[sm_idx] < nums2[res_idx]) {
            res_idx /= 2;
            if (res_idx == 0) break;
        }

        if (res_idx == 0) {
            cur_cnt += m/2 + 1; 
            nums1 += m/2 + 1; 
            m -= m/2 + 1; 
        }

        if (cur_cnt == total_cnt) {
            int n1 = m > 0 ? nums1[0] : INT_MAX;
            int n2 = n > 0 ? nums2[0] : INT_MAX;
            return fmin(n1, n2);
        }

        if (cur_cnt + res_idx + 1 < total_cnt) {
            nums2 += res_idx + 1;
            n -= res_idx + 1; 
            cur_cnt += res_idx + 1; 
        }        
    }

    return -1;

}

double findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {

    if ((m+n)%2 == 1) return _findMedianSortedArrays(nums1, m, nums2, n);

    int max1 = !m ? INT_MIN : nums1[m-1];
    int max2 = !n ? INT_MIN : nums2[n-1];
    int min1 = !m ? INT_MAX : nums1[0];
    int min2 = !n ? INT_MAX : nums2[0];

    double ans1, ans2; 
    if (min1 < min2) ans1 = _findMedianSortedArrays(nums1+1, m-1, nums2, n);
    else ans1 = _findMedianSortedArrays(nums1, m, nums2+1, n-1);

    if (max1 < max2) ans2 = _findMedianSortedArrays(nums1, m, nums2, n-1);
    else ans2 = _findMedianSortedArrays(nums1, m-1, nums2, n);

    #if DEBUG
    printf("ans1: %f and ans2: %f\n", ans1, ans2);   
    #endif 
    return (ans1 + ans2) / 2;
}

int main(int argc, char** argv) {

    int n1[100] = {1,2,3,4,5,6};
    int n2[100] = {1,2,4,5,6,7,8};

    printf("\nanswer is: %f", findMedianSortedArrays(n1, 4, n2, 4));
    return 0;
}