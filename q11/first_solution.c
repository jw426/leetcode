#include <math.h>

int maxArea(int* height, int heightSize) {

    int maxAmount = 0, i = 0, j = heightSize - 1;
    int area, min;
    while (i < j) {
        min = fmin(height[i], height[j]);
        area = min*(j-i);
        maxAmount = area > maxAmount ? area : maxAmount; 
        while (i < j && height[i] <= min) i++;
        while (i < j && height[j] <= min) j--;
    }

    return maxAmount; 
}
