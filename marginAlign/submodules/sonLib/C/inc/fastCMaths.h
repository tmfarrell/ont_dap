/*
 * Copyright (C) 2006-2012 by Benedict Paten (benedictpaten@gmail.com)
 *
 * Released under the MIT license, see LICENSE.txt
 */

/*This code is taken and adapted directly from the probcons library,
 * with an addition for random numbers.
 */

/////////////////////////////////////////////////////////////////
// FLOAT_32.h
//
// Routines for doing math operations in PROBCONS.
/////////////////////////////////////////////////////////////////

#ifndef FASTCMATHS_H
#define FASTCMATHS_H

#include <math.h>
#include <float.h>
#include <limits.h>
#include <stdlib.h>
#include <inttypes.h>

#ifdef __cplusplus
extern "C" {
#endif

#define TRUE 1
#define FALSE 0

#define LOG_ZERO -INFINITY //-1e300
//#define LOG_ZERO -1e30000
//-2e20
#define LOG_ONE 0.0
#define ZERO 0.0
#define ONE 1.0

#define INT_STRING "%" PRIi64

#define STRING_ARRAY_SIZE 100000
#define BIG_STRING_ARRAY_SIZE 10000000

#define TINY_CHUNK_SIZE 5
#define SMALL_CHUNK_SIZE 100
#define MEDIUM_CHUNK_SIZE 1000
#define LARGE_CHUNK_SIZE 1000000

/////////////////////////////////////////////////////////////////
// LOG()
//
// Compute the logarithm of x.
/////////////////////////////////////////////////////////////////

float LOG (float x);

/////////////////////////////////////////////////////////////////
// EXP()
//
// Computes exp(x).
/////////////////////////////////////////////////////////////////

float EXP (float x);

#define EXP_UNDERFLOW_THRESHOLD -4.6
#define LOG_UNDERFLOW_THRESHOLD 7.5

//const FLOAT_32 EXP_UNDERFLOW_THRESHOLD = -4.6;
//const FLOAT_32 LOG_UNDERFLOW_THRESHOLD = 7.5;

/////////////////////////////////////////////////////////////////
// LOOKUP()
//
// Computes log (exp (x) + 1), for 0 <= x <= 7.5.
/////////////////////////////////////////////////////////////////

float LOOKUP (float x);

/////////////////////////////////////////////////////////////////
// LOG_PLUS_EQUALS()
//
// Add two log probabilities and store in the first argument
/////////////////////////////////////////////////////////////////

void LOG_PLUS_EQUALS (float *x, float y);


/////////////////////////////////////////////////////////////////
// LOG_ADD()
//
// Add two log probabilities
/////////////////////////////////////////////////////////////////

float LOG_ADD (float x, float y);


/////////////////////////////////////////////////////////////////
// LOG_ADD()
//
// Add three log probabilities
/////////////////////////////////////////////////////////////////

float LOG_ADD_THREE (float x1, float x2, float x3);

/////////////////////////////////////////////////////////////////
// MAX_EQUALS()
//
// Chooses maximum of two arguments and stores it in the first argument
/////////////////////////////////////////////////////////////////

void MAX_PLUS_EQUALS (float *x, float y);

/////////////////////////////////////////////////////////////////
// RANDOM()
//
// Return random FLOAT_32 in range [0 - 1.0 }
/////////////////////////////////////////////////////////////////
float RANDOM(void);

/////////////////////////////////////////////////////////////////
// RANDOM()
//
// Return random FLOAT_32 in range [0 - 1.0 }
/////////////////////////////////////////////////////////////////
float RANDOM_LOG(void);

#ifdef __cplusplus
}
#endif
#endif
