// First solved May 13, 2026

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* new_arr = malloc(sizeof(int) * numsSize * 2);
    for(int i = 0; i < numsSize; i++) {
        new_arr[i] = nums[i];
        new_arr[i + numsSize] = nums[i];
    }
    *returnSize = numsSize * 2;
    return new_arr;    
}