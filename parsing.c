#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mpc.h"

#ifdef _WIN32
    /* Fake readline function */
    char* readline(char* prompt) {
        static char buffer[2048];
        fputs(prompt, stdout);
        fgets(buffer, 2048, stdin);
        char* cpy = malloc(strlen(buffer)+1);
        strcpy(cpy, buffer);
        cpy[strlen(cpy)-1] = '\0';
        return cpy;
    }

    /* Fake add_history function */
    void add_history(char* unused) {}

#elif __linux__  // Defined if the OS is Linux-based POSIX-compliant
    // #include <editline/readline.h>
    #include <readline/readline.h>
    // #include <histedit.h>
    #include <readline/history.h>
#endif


int main() {
	/* Create Some Parsers */
	mpc_parser_t *Number = mpc_new("number");
	mpc_parser_t *Operator = mpc_new("operator");
	mpc_parser_t *Expr = mpc_new("expr");
	mpc_parser_t *Lispy = mpc_new("lispy");


	/* Define them with the following Language */
	mpca_lang(MPCA_LANG_DEFAULT,
	        "\
	        number  : /-?[0-9]+/; \
	        operator: '+' | '-' | '*' | '/'; \
	        expr    : <number> | '('<operator><expr>+')'; \
	        lispy   : /^/ <operator> <expr>+ /$/ ; \
	        ",
	        Number, Operator, Expr, Lispy);

    fputs("Lispy REPL\nPress Ctrl-C to exit\n", stdout);

    while(1) {
        char *input = readline("lipsy> ");  // Output prompt
        add_history(input);  // Adding input to history

        if(strcmp(input, "version?") == 0) {
            puts("Lispy Version 0.0.0.0.1");
            continue;
        }

        else if(strcmp(input, "exit!") == 0) {
            exit(0);
        }
        
        mpc_result_t r;
        if(mpc_parse("<stdin>", input, Lispy, &r)) {
            /* On sucess print the AST */
            mpc_ast_print(r.output);
            mpc_ast_delete(r.output);
        }
        else {
            /* Otherwise print the error */
            mpc_err_print(r.error);
            mpc_err_delete(r.error);
        }
        // printf("%s\n", input);
        free(input);
    }
    
    mpc_cleanup(4, Number, Operator, Expr, Lispy);
    return 0;
}
