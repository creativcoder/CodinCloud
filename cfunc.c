#include<Python.h>


//Function to be called from python
static PyObject* py_myFunction(PyObject* self,PyObject* args)
{
	char *s="Hello from C!";
	return Py_BuildValue("s",s);
}
// another function to be called from python
static PyObject* py_myOtherFunction(PyObject* self,PyObject* args)
{
	double x,y;
	PyArg_ParseTuple(args,"dd",&x,&y);
	return Py_BuildValue("d",x*y);

	//char *s="Hello from C!";
	//return Py_BuildValue("s",s);
}

Bind python function names to our c function

static PyMethodDef myModule_methods[]={
	{"myFunction",py_myFunction,METH_VARARGS},
}
