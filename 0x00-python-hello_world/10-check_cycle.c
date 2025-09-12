#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *check_cycle - checks if there is a cycle in a singly linked list
 *@list: the linked list
 *Return: 1-true 0-false
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while(fast != NULL && slow != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
