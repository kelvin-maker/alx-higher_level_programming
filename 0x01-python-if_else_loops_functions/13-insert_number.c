#include "lists.h"

listint_t *_insert_node(listint_t **head, int number)
{
  listint_t *new;

  if (*head && number > (*head)->n)
    return (_insert_node(&((*head)->next), number));

  new = malloc(sizeof(*new));
  if (!new)
    return (NULL);

  new->n = number;
  new->next = *head;
  *head = new;

  return (new);
}

listint_t *insert_node(listint_t **head, int number)
{
  if (head)
    return (_insert_node(head, number));
  return (NULL);
}
