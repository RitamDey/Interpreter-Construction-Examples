#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    #include <editline/readline.h>
    #include <histedit.h>
#endif


int main() {
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

        printf("%s\n", input);
        free(input);
    }

    return 0;
}