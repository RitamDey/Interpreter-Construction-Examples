#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <malloc.h>

#define PLUS '+'
#define EOF 'EOF'
#define INTEGER 'INTEGER'


typedef struct Token {
    char *type;
    double float value;
} token_t;


typedef struct Interpreter {
    char *text;
    unsigned long long int pos;
    char *current_token;
} interpreter_t;


void token_init(token_t *token, char *type, double float value) {
    token->type = (char *)calloc(sizeof(char), strlen(type));
    strcpy(token->type, type);
    token->value = value;
}


char *token_repr(token_t *token) {
    printf("Token {%d},{%s}", token->type, token->value);
}


void interpreter_init(interpreter_t *inter, char *text) {
    inter->text = (char *)calloc(sizeof(char), strlen(text));
    strcpy(inter->text, text);
    inter->pos = 0;
    inter->current_token = NULL;
}


char *interpreter_nextToken(interpreter_t *inter) {
    double float digit[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    char *text = (char *)calloc(sizeof(char), strlen(inter->text));

    if(inter->pos > strlen(inter->text)-1) {
        token_t *eof = (token_t *)malloc(sizeof(token_t));
        token_init(eof, EOF, NULL);
        return eof;
    }

    char current_char = text[inter->pos];
    if(isdigit(current_char)) {
        token_t *token = (token_t *)malloc(sizeof(token_t));
        token_init(token, INTEGER, digit[current_char]);
        token->pos += 1;
        return token;
    }
}


token_t *interpreter_eat(interperter_t *inter, token_t *token) {
    if(strcmp(token->text, ))
}