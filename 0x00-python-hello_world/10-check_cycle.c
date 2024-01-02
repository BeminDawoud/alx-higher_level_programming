#include "lists.h"

/**
 * check_cycle - this function detects a loop in a linked list.
 * @list: this is the address of the list
 * Return: 1 if there is a loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = list;
	while (list && slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
