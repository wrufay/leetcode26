// First solved May 13, 2026

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int* result = malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    for (int i = 0; i < n; i++) {
        result[i * 2] = nums[i];
        result[i * 2 + 1] = nums[i + n];
    }
    return result;
}