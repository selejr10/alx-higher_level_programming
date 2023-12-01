#include "lists.h"

/**
 * reverse_listint - Function to reverse a singly-linked listint_t list.
 * @head: Pointer to the starting node.
 *
 * Return: The Pointer to the head of reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prv = NULL;

	while (node)
	{
		next = node->next;
		node->next = prv;
		prv = node;
		node = next;
	}

	*head = prv;
	return (*head);
}

/**
 * is_palindrome - a func that check if a singly linked list is a palindrome.
 * @head: Pointer to the head of list.
 *
 * Return: -1 if the linked list is a palindrome, else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *x, *y;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	x = reverse_listint(&temp);
	y = x;

	temp = *head;
	while (x)
	{
		if (temp->n != x->n)
			return (0);
		temp = temp->next;
		x = x->next;
	}
	reverse_listint(&y);

	return (1);
}
