#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <string.h>

/**
 *insert_node - insert a number into a sorted singly linked list
 *@head: the head of the linked list
 *@number: the number to insert
 *Return: the address of the new node
 */



listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *temp1;

	if (temp == NULL)
	{
		*head = malloc(sizeof(listint_t));
		if (*head == NULL)
		{
			return (NULL);
		}
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	if (temp->n > number)
	{
		temp1 = malloc(sizeof(listint_t));
		if (temp1 == NULL)
		{
			return (NULL);
		}
		temp1->next = temp;
		temp1->n = number;
		*head = temp1;
		return (temp1);
	}
        while (temp != NULL)
	{
		if (temp->next->n > number)
		{
			temp1 = malloc(sizeof(listint_t));
			if (temp1 == NULL)
			{
				return (NULL);
			}
			temp1->next = temp->next;
			temp1->n = number;
			temp->next = temp1;
			return (temp1);
		}
		temp = temp->next;
	}
	return (*head);
}
