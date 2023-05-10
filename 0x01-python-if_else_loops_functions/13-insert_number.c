#include "lists.h"

/**
* insert_node - inserts  node to a sorted singly linked list
* @head: head of the singly linked list.
* @number: the number to be inserted.
* Return: address of the new node.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *first;

	first = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || first->n > newNode->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (first->next != NULL)
	{
		if ((first->next->n > newNode->n && first->n < newNode->n)
			|| newNode->n == first->n)
		{
			newNode->next = first->next;
			first->next = newNode;
			return (newNode);
		}
		first = first->next;
	}
	newNode->next = first->next;
	first->next = newNode;
	return (newNode);
}