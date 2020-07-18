#include<semaphore.h>
class Foo {
public:
    sem_t s1;
    sem_t s2;
    Foo() {
        sem_init(&s1, 0, 0);
        sem_init(&s2, 0, 0);
    }

    void first(function<void()> printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        
        printFirst();
        sem_post(&s1);
    }

    void second(function<void()> printSecond) {
        
        // printSecond() outputs "second". Do not change or remove this line.
        sem_wait(&s1);
        printSecond();
        sem_post(&s2);
    }

    void third(function<void()> printThird) {
        
        // printThird() outputs "third". Do not change or remove this line.

        sem_wait(&s2);
        printThird();
    }
};