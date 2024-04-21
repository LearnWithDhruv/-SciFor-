#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100 // Maximum size of the stack

// Structure to represent the stack
typedef struct {
    int arr[MAX_SIZE]; // Array to store stack elements
    int top; // Index of the top element
} Stack;

// Function to initialize an empty stack
void initialize(Stack *stack) {
    stack->top = -1; // Initialize top as -1 to indicate an empty stack
}

// Function to check if the stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Function to check if the stack is full
int isFull(Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

// Function to push an element onto the stack
void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack Overflow: Cannot push element %d, stack is full.\n", value);
        return;
    }
    stack->arr[++stack->top] = value;
    printf("Pushed element %d onto the stack.\n", value);
}

// Function to pop an element from the stack
int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow: Cannot pop element, stack is empty.\n");
        return -1;
    }
    int poppedElement = stack->arr[stack->top--];
    printf("Popped element %d from the stack.\n", poppedElement);
    return poppedElement;
}

// Function to peek at the top element of the stack without removing it
int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty.\n");
        return -1;
    }
    return stack->arr[stack->top];
}

// Function to display all elements in the stack
void display(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Elements in the stack: ");
    for (int i = stack->top; i >= 0; i--) {
        printf("%d ", stack->arr[i]);
    }
    printf("\n");
}

int main() {
    Stack stack;
    initialize(&stack);

    // Perform stack operations
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    display(&stack);
    printf("Top element of the stack: %d\n", peek(&stack));
    pop(&stack);
    display(&stack);
    printf("Top element of the stack: %d\n", peek(&stack));
    pop(&stack);
    pop(&stack);
    pop(&stack); // Trying to pop from an empty stack
    display(&stack);

    return 0;
}
