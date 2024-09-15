#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: Pointer to a Python object, assumed to be a list.
 * 
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Error: Object is not a Python list\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    
    // Get the allocated size
    printf("[*] Allocated = %zd\n", PyList_GET_SIZE(p)); 

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
