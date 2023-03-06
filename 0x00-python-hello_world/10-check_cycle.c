#include "lists.h"
/**
 * check_cycle - checks a linked list for a cycle
 * @list: list to be checked
 * Return: 0 if no loop exists, 1 if a loop does exist
 */
int check_cycle(listint_t *list)
{
	listint_t *duplist = list;

	while (list && list->next)
	{
		list = list->next->next;
		duplist = duplist->next;
		if (list == duplist)
			return (1);
	}
	return (0);
}
