import threading 
import os 

def task1():
    print("Tarea 1 asignada al thread 1: {}".format(threading.current_thread().name))
    print("Id del hilo corriendo la tarea 1: {}".format(threading.current_thread().ident))

def tassk2():
    print("Tarea 2 asignada al thread : {}".format(threading.current_thread().name))
    print("Id del hilo corriendo la tarea 2: {}".format(threading.current_thread().ident))

if __name__ == "__main__":  
    print("ID del proceso corriendo el hilo main: {}".format(os.getpid()))
    print("Id del hilo corriendo la tarea el programa main: {}".format(threading.current_thread().ident))
    print("Nombre del Main thread: {}".format(threading.current_thread().name))

t1 = threading.Thread(target = task1, name = "Hilo1")
t2 = threading.Thread(target= tassk2, name = "Hilo2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Programa terminado")