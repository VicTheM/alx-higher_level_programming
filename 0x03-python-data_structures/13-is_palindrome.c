#include <stdlib.h>
#include "lists.h"

/**
 * even_palindrome - is_palindrome for str of even len
 * @head: head
 * @buf: first half of all elements in list
 * @len: len of list
 *
 * Return: 1 True - 0 False
 */
int even_palindrome(listint_t *head, int **buf, unsigned int len)
{
	unsigned int c;

	*buf = malloc((len / 2) * sizeof(int));
	if (buf == NULL)
		return (0);
	for (c = 0; c < len / 2; c++)
	{
		*(*buf + c) = head->n;
		head = head->next;
	}

	while (c > 0 && head != NULL)
	{
		c--;
		if (head->n != *(*buf + c))
		{
			free(*buf);
			return (0);
		}
		head = head->next;
	}
	free(*buf);
	return (1);

}

/**
 * odd_palindrome - is_palindrome for str of odd len
 * @head: head
 * @buf: the first half items in list
 * @len: len of str
 * Description: this function only works for odd strings
 * with len > 2
 *
 * Return: 1 True - 0 False
 */
int odd_palindrome(listint_t *head, int **buf, unsigned int len)
{
	unsigned int c;

	*buf = malloc((len / 2) * sizeof(int));
	if (*buf == NULL)
		return (0);

	for (c = 0; c < len / 2; c++)
	{
		*(*buf + c) = head->n;
		head = head->next;
	}
	head = head->next;

	while (c > 0 && head != NULL)
	{
		c--;
		if (head->n != *(*buf + c))
		{
			free(*buf);
			return (0);
		}
		head = head->next;
	}
	free(*buf);
	return (1);

}

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: address of pointer to head node
 *
 * Return: 1 if True, else 0
 */
int is_palindrome(listint_t **head)
{
	unsigned int len;
	int *buf;
	listint_t *first, *last;

	if (!(head || *head))
		return (0);
	first = last = *head;
	if (first == NULL)
		return (1);

	for (len = 1; last->next != NULL; last = last->next)
		len++;

	if (len % 2 != 0)
		return (odd_palindrome(first, &buf, len));
	else
		return (even_palindrome(first, &buf, len));
}
