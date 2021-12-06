; utility functions
(define (print x) (display x) (newline))
(define (repeat n f) (if (= n 0) '() (begin (f) (repeat (- n 1) f))))
(define (ignore-chars n f) (repeat n (lambda () (read-char f))))
(define (tails ls) (if (null? ls) '() (cons ls (tails (cdr ls)))))
(define (between a b x) (or (and (<= a x) (<= x b)) (and (>= a x) (>= x b))))

(define (range a b)
  (cond ((< a b) (cons a (range (+ a 1) b)))
        ((> a b) (cons a (range (- a 1) b)))
        (else (list a))))

; given (a b c d ...) and f, does (f a b), (f a c) (f a d) ... (f b c), (f b d) ...
(define (for-all-pairs f x)
  (define (pairs ls) (map (lambda (x) (f (car ls) x)) (cdr ls)))
  (map pairs (tails x)))

; point (x, y)
(define (point x y) (list x y))

; line segment object from (x1, y2) to (x2, y2)
(define (line-segment x1 y1 x2 y2) (list x1 y1 x2 y2))
(define x1 car)
(define y1 cadr)
(define x2 caddr)
(define y2 cadddr)

(define (read-line-segment f)
  (let* ((x1 (read f))
         (y1 (begin (read-char f) (read f)))
         (x2 (begin (ignore-chars 4 f) (read f)))
         (y2 (begin (read-char f) (read f))))
    (read-char f) ; eat newline
    (line-segment x1 y1 x2 y2)))

(define (vertical? l) (= (x1 l) (x2 l)))
(define (horizontal? l) (= (y1 l) (y2 l)))
(define (diagonal? l) (not (or (vertical? l) (horizontal? l))))

; read results into a list until eof
(define (read-all readfn f)
  (define (iter acc)
    (if (eof-object? (peek-char f))
      acc
      (iter (cons (readfn f) acc))))
  (iter '()))

(define (intersecting? p q)
  (cond
    ((and (vertical? p) (vertical? q))
     (and (= (x1 p) (x1 q)) (or (between (y1 q) (y2 q) (y1 p)) (between (y1 q) (y2 q) (y2 p)))))
    ((and (horizontal? p) (horizontal? q))
     (and (= (y1 p) (y1 q)) (or (between (x1 q) (x2 q) (x1 p)) (between (x1 q) (x2 q) (x2 p)))))
    ((and (vertical? p) (horizontal? q))
     (and (between (y1 p) (y2 p) (y1 q)) (between (x1 q) (x2 q) (x1 p))))
    ((and (horizontal? p) (vertical? q))
     (and (between (y1 q) (y2 q) (y1 p)) (between (x1 p) (x2 p) (x1 q))))
    (else #f)))

(define (num-intersections p q)
  (cond
    ((and (vertical? p) (horizontal? q) (intersecting? p q)) 1)
    ((and (horizontal? p) (vertical? q) (intersecting? p q)) 1)
    ((and (vertical? p) (vertical? q) (intersecting? p q))
     (let ((y-coords (sort (list (y1 p) (y2 p) (y1 q) (y2 q)) <))) (+ 1 (- (caddr y-coords) (cadr y-coords)))))
    ((and (horizontal? p) (horizontal? q) (intersecting? p q))
     (let ((x-coords (sort (list (x1 p) (x2 p) (x1 q) (x2 q)) <))) (+ 1 (- (caddr x-coords) (cadr x-coords)))))
    (else 0)))

; returns a list of the intersecting points of lines p and q
(define (all-intersections p q)
  (define n (num-intersections p q))
  (cond ((= n 0) '())
        ((and (vertical? p) (horizontal? q)) (list (x1 p) (y1 q)))
        ((and (horizontal? p) (vertical? q)) (list (y1 p) (x1 q)))
        ((and (vertical? p) (vertical? q))
         (let ((y-coords (sort (list (y1 p) (y2 p) (y1 q) (y2 q)) <)))
           (map (lambda (y) (list (x1 p) y)) (range (caddr y-coords) (cadr y-coords)))
           ))
        ((and (horizontal? p) (horizontal? q))
         (let ((x-coords (sort (list (x1 p) (x2 p) (x1 q) (x2 q)) <)))
           (map (lambda (x) (list (y1 p) x)) (range (caddr x-coords) (cadr x-coords)))))))

(define (solA lines)
  (define intersections (make-equal-hash-table))

  )

(call-with-input-file "day5.in"
  (lambda (f)
    (define lines (filter (lambda (x) (not (diagonal? x))) (read-all read-line-segment f)))
    ; (for-all-pairs (lambda (x y) (display x) (display y) (print (all-intersections x y))) lines)
    (for-all-pairs (lambda (x y) (all-intersections x y)) lines)
    ))

