/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <string.h>

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    
    // length of all words in list
    int concat_strlen = 0;
    for (int i = 0; i < wordsSize; i++) {
        concat_strlen += strlen(words[i]);
    }

    // string length limit
    if (strlen(s) < concat_strlen) return NULL;

        
}