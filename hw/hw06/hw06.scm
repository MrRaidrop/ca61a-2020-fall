(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s )))
)


(define (sign num)
  (cond ((> num 0) 1)
        ((= num 0) 0)
        (else -1)
        )
)


(define (square x) (* x x))

(define (pow x y)
    (cond ((= x 1) 1)
          ((= y 1) x)
          ((= 1 (modulo y 2))(* x (square (pow x (quotient (- y 1) 2)))))
          ((= 0 (modulo y 2))(square (pow x (quotient y 2))))
          )
)

