#include <stdio.h>
#include <stdlib.h>

#define PLUS 1
#define EOF EOF

typedef struct Token {
    int type;
    double float value;
} token_t;


typedef struct Interpreter {
    char *text;
    unsigned long long int pos;
    char *current_token;
} interpreter_t;


void token_init(token_t *token, type, value) {
    token->type = type;
    token->value = value;
}


char *token_repr(token_t *token) {
    printf("Token {%d},{%s}", token->type, token->value);
}


void interpreter_init(interpreter_t *inter, char *text) {
    
}