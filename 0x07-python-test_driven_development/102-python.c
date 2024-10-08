#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints a Python string.
 * @p: A PyObject pointer to the Python object.
 *
 * This function prints the type and value of the given Python string.
 * If the object is not a string, an error message is printed.
 */
void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))  // Check if p is a Unicode string
    {
        const char *str = PyUnicode_AsUTF8(p);  // Convert to UTF-8 string
        Py_ssize_t length = PyUnicode_GetLength(p);  // Get the length of the string

        // Print the type and value
        printf("[.] string object info\n");
        printf("  type: %s\n", "string");
        printf("  length: %zd\n", length);
        printf("  value: %s\n", str);
    }
    else
    {
        // Print error message if p is not a string
        printf("Invalid Python string object\n");
    }
}
