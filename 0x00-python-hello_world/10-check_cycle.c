#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: this is the pointer to the head of the linked list
 * Return: 0 if there is no cycle and 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step_ptr = list;
	listint_t *two_step_ptr = list;

	while (one_step_ptr && two_step_ptr && two_step_ptr->next)
	{
		one_step_ptr = one_step_ptr->next;
		two_step_ptr = two_step_ptr->next->next;
		if (one_step_ptr == two_step_ptr)
			return (1);
	}
	return (0);
}
