#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: Address of the new node, NULLon failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *m = *head, *nnode;

	nnode = malloc(sizeof(listint_t));
	if (nnode == NULL)
		return (NULL);
	nnode->n = number;
	if (m == NULL || m->n >= number)
	{
		nnode->next = m;
		*head = nnode;
		return (nnode);
	}

	while (m && m->next && m->next->n < number)
		m = m->next;

	nnode->next = m->next;
	m->next = nnode;
	return (nnode);
}
