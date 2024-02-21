#include <math.h>
#include <limits.h>
#include <stdio.h>

double med(int* nums, int n) {

    return nums[n/2];
}

void print_array(int* nums, int n) {
    for (int i = 0; i<n; i++) {
        printf(" %d ", nums[i]);
    }
    printf("\n");
}

double _findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {
    
    printf("%d, %d\n", m, n);
    print_array(nums1, m);
    print_array(nums2, n);
    // base case
    if (m==1 && n==1) return fmax(nums1[0], nums2[0]);
    if (m<=0) return med(nums2, n);
    if (n<=0) return med(nums1, m);

    // case when m+n is odd

    if (nums1[m/2] < nums2[n/2]) {
        return _findMedianSortedArrays(nums1+m/2, m-m/2, nums2, n/2); 
    } else if (nums1[m/2] > nums2[n/2]) {
        return _findMedianSortedArrays(nums1, m/2, nums2+n/2, n-n/2);
    } else {
        return fmax(nums1[m/2], nums2[n/2]);
    }

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

    printf("ans1: %f and ans2: %f\n", ans1, ans2);    
    return (ans1 + ans2) / 2;
}

int main(int argc, char** argv) {

    int n1[100] = {1,2,3,4,5,6};
    int n2[100] = {1,2,4,5,6,7,8};

    printf("\nanswer is: %f", findMedianSortedArrays(n1, 4, n2, 4));
    return 0;
}