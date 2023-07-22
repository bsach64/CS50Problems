// Implements a dictionary's functionality
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1125;
unsigned int dict_word_count;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    /*
        1. Return true if the word is in the dictionary, else false.
        2. Function should be case-insensitive.
        1. Hash word to obtain a hash value.
        2. Access linked list at that index in the hash table.
        3. Traverse linked list, looking for the word (strcasecmp)
    */
    unsigned int hash_value = hash(word);
    node *trav  = table[hash_value];
    bool found = false;
    do
    {
        if (strcasecmp(trav->word, word) == 0)
        {
            found = true;
            break;
        }
        else
        {
            trav = trav->next;
        }
    }
    while (trav != NULL);
    return found;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    /*
        1. Take as input: a word with alphabetical characters and (possibly) apstrophes
        2. Return an positive integer between 0 & N - 1 inclusive.
    */

    char copy[LENGTH + 1];
    unsigned int hash_number_one = 0;
    unsigned int hash_number_two = 0;
    unsigned int final_hash = 0;
    strcpy(copy, word);
    for (int i = 0; i < strlen(word); i++)
    {
        copy[i] = tolower(copy[i]);
    }
    for (int i = 0; i < 26; i++)
    {
        if (copy[0] - 97 == i)
        {
            hash_number_one = i;
        }
        final_hash = hash_number_one;
    }
    return final_hash;

    /*char copy[LENGTH + 1];
    int hash_number_one = 0;
    int hash_number_two = 0;
    int final_hash = 0;
    strcpy(copy, word);
    for (int i = 0; i < strlen(copy); i++)
    {
        copy[i] = tolower(word[i]);
    }
    for (int i = 0; i < 26; i++)
    {
        if (copy[0] - 97 == i)
        {
            hash_number_one = i;
        }
        if (strlen(copy) > 1)
        {
            if (copy[1] - 97 == i)
            {
                hash_number_two = i;
            }
            final_hash = 26 * (hash_number_one) + hash_number_two;
        }
        else
        {
            final_hash = hash_number_one;
        }
    }
    return final_hash % 676;*/
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    /*
        1. Open dictionary file
            1. Use fopen
            2. Check if it returned NULL
        2. Read strings from file one at a time.
            1. Use fscanf(file, "%s", word)
            2. Do (1) until fscanf returns EOF
        3. Create a new node for each word.
            1. Use malloc to allocate memory
            2. Remember to check if return value is NULL.
            3. Copy word into node using strcpy.
        4. Hash word to obtain a hash value.
            1. Use the hash function.
            2. Function takes a string and returns an index.
        5. Insert node into hash table at that location.
            1. Recall that hash table is an array of linked lists.
            2. Be sure to set pointers in the correct order.
    */
    dict_word_count = 0;
    FILE *dict_pointer = fopen(dictionary, "r");
    if (dict_pointer != NULL)
    {
        char temp[LENGTH + 1];
        int scan_count = 0;
        do
        {
            scan_count = fscanf(dict_pointer, "%s", temp);
            if (scan_count != EOF)
            {
                dict_word_count++;
                unsigned int hash_value = hash(temp);
                node *temp_pointer = table[hash_value];
                node *new_node = malloc(sizeof(node));
                if (new_node == NULL)
                {
                    fclose(dict_pointer);
                    return false;
                }
                strcpy(new_node->word, temp);
                new_node->next = temp_pointer;
                table[hash_value] = new_node;
            }
        }
        while (scan_count != EOF);
        fclose(dict_pointer);
        return true;
    }
    else
    {
        fclose(dict_pointer);
        return false;
    }
    fclose(dict_pointer);
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return dict_word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    /*

    */
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }
    return true;
}
