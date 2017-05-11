#-*- utf-8 -*-

def generator():
    name = 1
    while True and name < 10 :
        yield name
        name = name + 1

if __name__ == '__main__':
    gen = generator()
    print gen.next()
    print gen.next()
    print gen.next()

    print '~~~~~~~~~~~'
    for i in gen:
        print i

'''
在解释生成器之前，需要讲解一下Python虚拟机的调用原理。

Python虚拟机有一个栈帧的调用栈，其中栈帧的是PyFrameObject，位于Include/frameobject.h。

typedef struct _frame {
    PyObject_VAR_HEAD
    struct _frame *f_back;  /* previous frame, or NULL */
    PyCodeObject *f_code;   /* code segment */
    PyObject *f_builtins;   /* builtin symbol table (PyDictObject) */
    PyObject *f_globals;    /* global symbol table (PyDictObject) */
    PyObject *f_locals;     /* local symbol table (any mapping) */
    PyObject **f_valuestack;    /* points after the last local */
    /* Next free slot in f_valuestack.  Frame creation sets to f_valuestack.
       Frame evaluation usually NULLs it, but a frame that yields sets it
       to the current stack top. */
    PyObject **f_stacktop;
    PyObject *f_trace;      /* Trace function */
 
    /* If an exception is raised in this frame, the next three are used to
     * record the exception info (if any) originally in the thread state.  See
     * comments before set_exc_info() -- it's not obvious.
     * Invariant:  if _type is NULL, then so are _value and _traceback.
     * Desired invariant:  all three are NULL, or all three are non-NULL.  That
     * one isn't currently true, but "should be".
     */
    PyObject *f_exc_type, *f_exc_value, *f_exc_traceback;
 
    PyThreadState *f_tstate;
    int f_lasti;        /* Last instruction if called */
    /* Call PyFrame_GetLineNumber() instead of reading this field
       directly.  As of 2.3 f_lineno is only valid when tracing is
       active (i.e. when f_trace is set).  At other times we use
       PyCode_Addr2Line to calculate the line from the current
       bytecode index. */
    int f_lineno;       /* Current line number */
    int f_iblock;       /* index in f_blockstack */
    PyTryBlock f_blockstack[CO_MAXBLOCKS]; /* for try and loop blocks */
    PyObject *f_localsplus[1];  /* locals+stack, dynamically sized */
} PyFrameObject;

    栈帧保存了给出代码的的信息和上下文，其中包含最后执行的指令，全局和局部命名空间，异常状态等信息。
    f_valueblock保存了数据，b_blockstack保存了异常和循环控制方法。
    那么，相应的调用栈如下，一个py文件，一个类，一个函数都是一个代码块，对应者一个Frame，保存着上下文环境以及字节码指令。
'''