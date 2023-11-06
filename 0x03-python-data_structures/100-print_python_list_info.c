#include <Python.h>
/**
 * print_python_list_info - Print information about a Python list.
 * @p: A pointer to a PyObject (Python list).
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *px = (PyListObject *)p;
    Py_ssize_t size_x, allocated_x, i_x;
    PyObject *item_x;

    size_x = Py_SIZE(px);
    allocated_x = px->allocated;

    printf("[*] Size of the Python List = %ld\n", size_x);
    printf("[*] Allocated = %ld\n", allocated_x);

    i_x = 0;
    while (i_x < size_x) {
        item_x = PyList_GET_ITEM(p, i_x);
        printf("Element %ld: %s\n", i_x, Py_TYPE(item_x)->tp_name);
        i_x++;
    }
}
