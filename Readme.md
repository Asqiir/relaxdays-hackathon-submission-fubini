This project was created in the Relaxdays Code Challenge Vol. 1. See https://sites.google.com/relaxdays.de/hackathon-relaxdays/startseite for more information. My participant ID in the challenge was: CC-VOL1-37.

# Idea

This program is supposed to calculate the first `n` [Fubini](https://en.wikipedia.org/wiki/Ordered_Bell_number) numbers.

I use this formula found on [Wikipedia](https://en.wikipedia.org/wiki/Ordered_Bell_number#Recurrence_and_modular_periodicity):

<img alt="a(n) = \sum_{i=1}^n {n \choose i} \cdot a(n-i)" src="https://latex.codecogs.com/gif.latex?a(n)&space;=&space;\sum_{i=1}^n&space;{n&space;\choose&space;i}&space;\cdot&space;a(n-i)" />

Instead of recursion I use dynamic programming to determine a(0) first, then a(1), ... up to a(n).

Before doing any of this I calculate the Binomal coeffictient j over k for every j and k from 0 to n.

# How to run this project

## Prerequisites

* Docker

## Commands to run

```bash
git clone https://github.com/Asqiir/relaxdays-hackathon-submission.git
cd relaxdays-hackathon-submission-fubini
docker build -t fubini .
docker run fubini <n>
```

Replace `<n>` with an integer larger as 0.