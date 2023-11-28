#include "lists.h"

/**
 * check_cycle - ...
 * @head: list
 *
 * Return: 0, no head otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (NULL);
/* floyed cycle detection */
	slow = fast = list;
	while (fast && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
