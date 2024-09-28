#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information
 * about a Python list.
 *
 * @p: A pointer to the Python list object to be printed.
 *
 * This function checks if the provided PyObject
 * is a valid Python list.
 * If valid, it prints the following information:
 * 1. The size of the list (number of elements).
 * 2. The allocated size of the list (memory allocation).
 * 3. The type of each element in the list.
 *
 * If the provided PyObject is not a
 * valid list, it prints an error message.
 */
void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
printf("Invalid PyObject. Not a list.\n");
return;
}

Py_ssize_t size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the list: %zd\n", size);
printf("[*] Allocated: %zd\n", ((PyListObject *)p)->allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - Prints information about
 * a Python bytes object.
 *
 * @p: A pointer to the Python bytes objectto be printed.
 *
 * This function checks if the provided PyObject
 * is a valid Python bytes object.
 * If valid, it prints the following information:
 * 1. The total size of the bytes object (number of bytes).
 * 2. The first 10 bytes of the object in
 * hexadecimal format. If the total size
 * is less than 10, it prints all available bytes.
 *
 *i If the provided PyObject is not
 * valid bytes object, it prints an error message.
 */


void print_python_bytes(PyObject *p)
{
if (!PyBytes_Check(p))
{
printf("Invalid PyObject. Not a bytes object.\n");
return;
}

Py_ssize_t size = PyBytes_Size(p);
printf("[.] bytes object info\n");
printf("[.] Size: %zd\n", size);
printf("[.] First %zd bytes: ", size > 10 ? 10 : size);

for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
{
printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
if (i < (size > 10 ? 9 : size - 1))
{
printf(" ");
}
}
printf("\n");
}
