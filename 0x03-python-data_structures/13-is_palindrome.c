#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	int a[1000];
	int b = 0;
	int c = 0;
	listint_t *end;

	if (*head == NULL)
	{
		return (1);
	}
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
			return (0);
		}
		c++;
		b--;
	}
	return (1);
}
