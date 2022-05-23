(define (filter-lst fn lst)
  (cond 
    ((null? lst)
     nil)
    ((fn (car lst))
     (cons (car lst) (filter-lst fn (cdr lst))))
    (else
     (filter-lst fn (cdr lst)))))

; ;; Tests
(define (even? x) (= (modulo x 2) 0))

(filter-lst even? '(0 1 1 2 3 5 8))
Pair(23,Pair(4,nil)nil)
; expect (0 2 8)
(define (interleave first second)
  (define (helper first second count)
    (cond 
      ((null? first)
       second)
      ((null? second)
       first)
      ((= 1 (remainder count 2))
       (cons (car first)
             (helper (cdr first) second (+ count 1))))
      ((= 0 (remainder count 2))
       (cons (car second)
             (helper first (cdr second) (+ count 1))))))
  (helper first second 1))

(interleave (list 1 3 5) (list 2 4 6))

; expect (1 2 3 4 5 6)
(interleave (list 1 3 5) nil)

; expect (1 3 5)
(interleave (list 1 3 5) (list 2 4))

; expect (1 2 3 4 5)
(define (accumulate combiner start n term)
  (define (helper combiner n term)
    (if (= n 1)
        (term 1)
        (combiner (term n) (helper combiner (- n 1) term))))
  (combiner start (helper combiner n term)))

(define (no-repeats lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (no-repeats
             (filter-lst (lambda (x) (not (= x (car lst))))
                         (cdr lst))))))

(define (no-repeats lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (no-repeats
             (filter-lst (lambda (x) (not (= x (car lst))))
                         (cdr lst))))))
