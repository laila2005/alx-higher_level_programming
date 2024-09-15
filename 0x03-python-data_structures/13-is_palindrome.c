#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * 
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * 
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *second_half;
    listint_t *prev_of_slow = NULL;
    listint_t *middle = NULL;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    second_half = reverse_list(slow);
    prev_of_slow->next = second_half;

    listint_t *first_half = *head;
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    second_half = reverse_list(prev_of_slow->next);
    prev_of_slow->next = second_half;

    if (middle != NULL)
    {
        prev_of_slow->next = middle;
        middle->next = second_half;
    }

    return (palindrome);
}
