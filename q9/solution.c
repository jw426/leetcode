#include <string.h>

int check(char sch, char pch);
char* reduce(char p[]);
int isMatch(char* s, char* p);

int isMatch(char* s, char* p) {

    int j = 0;

    for (int i = 0; i < strlen(p); i++) {

        if (p[i] == '*') {
            if (i == 0 || p[i-1] == '*') continue; 
            
            if (isMatch(s+j, p+i+1)) return 1;
            while (j < strlen(s) && check(s[j], p[i-1])) {
                if (isMatch(s+(++j), p+i+1)) return 1;
            }
            return 0;

        } else {
            if (i < strlen(p) - 1 && p[i+1] == '*') continue;
            if (j == strlen(s) || (j < strlen(s) && !check(s[j], p[i]))) return 0;
            j++;
        }
    }

    return (strlen(s+j) == 0);
}

int check(char sch, char pch) {
    if (pch == '.') return true; 
    if (sch == pch) return true; 
    return false;
}

char* reduce(char p[]) {

    int orig = 0; 
    int comp = 2;
    while (orig < strlen(p)) {
        while (comp + 1 < strlen(p)) {
            if (p[orig + 1] == '*' && p[comp + 1] == '*' && p[orig] == p[comp]) {
                comp += 2; 
            } else break;
        }
        if (comp > orig + 2) strcpy(p + orig + 2, p + comp);
        orig++;
        comp = orig + 2; 
    }
    return p;
}