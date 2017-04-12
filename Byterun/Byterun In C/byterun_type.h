#ifndef BYTERUN_TYPES_H
#define BYTERUN_TYPES_H

#include <stdint.h>


typedef struct ByteObject_Object {
    size_t type_size;
    uintmax_t ref_count;
} ByteObject_Object;


typedef struct ByteObject_Int {
    ByteObject_Object;
    long long long int data;

    struct ByteObject_Int *(tp_new)(void);
    struct ByteObject_Int *(tp_init)(struct ByteObject_Int *self);

    ByteObject
} ByteObject_Int;

#endif