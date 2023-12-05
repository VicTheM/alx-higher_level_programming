#include <Python.h>

/**
 * print_python_list_info - Prints info about a python list
 * @p: PythonObject
 */
void print_python_list_info(PyObject *p)
{
		PyListObject *pp = (PyListObject *)p;
		long int size = PyList_Size(p);
		int i;

		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", pp->allocated);

		for (i = 0; i < size; i++)
		{
			printf("Element %i: %s\n", i, Py_TYPE(pp->ob_item[i])->tp_name);
		}
}
