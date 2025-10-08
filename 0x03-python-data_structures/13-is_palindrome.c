#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome)= - checks if a linked list is a palindrome
 *@head: pointer to the linked list
 *Return: 0-false, 1-true
 */

int is_palindrome(listint_t **head)
{
	int *a;
	int b = 0;
	int c = 0;
	listint_t *end;

	if (*head == NULL || head == NULL)
	{
		return (1);
	}
	end = *head;
	while (end != NULL)
	{
		end = end->next;
		b++;
	}
	a = malloc(b * sizeof(int));
	if (a == NULL)
	{
		return (0);
	}
	b = 0;
	end = *head;
	while (end != NULL)
	{
		a[b] = end->n;
		end = end->next;
		b++;
	}
	b--;
	while (c < b)
	{
		if (a[c] != a[b])
		{
			free(a)
			return (0);
		}
		c++;
		b--;
	}
	free(a);
	return (1);
}
