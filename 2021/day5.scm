; utility functions
(define (print x) (display x) (newline))
(define (repeat n f) (if (= n 0) '() (begin (f) (repeat (- n 1) f))))
(define (ignore-chars n f) (repeat n (lambda () (read-char f))))
(define (between a b x) (or (and (<= a x) (<= x b)) (and (>= a x) (>= x b))))
(define (inc x) (+ 1 x))
(define (dec x) (- x 1))
(define (sum ls) (reduce + 0 ls))

(define (vector-count pred? v)
  (sum (map (lambda (idx)
              (let ((x (vector-ref v idx)))
                (if (pred? x) 1 0)))
            (range 0 (- (vector-length v) 1)))))

(define (range a b)
  (define (iter x y acc)
    (cond ((< x y) (iter (inc x) y (cons x acc)))
          ((> x y) (iter x (inc y) (cons y acc)))
          (else (cons x acc))))
  (if (< a b) (iter a b '()) (reverse (iter a b '()))))

(define (point x y) (list x y))
(define x car)
(define y cadr)

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
(define (diagonal? l) (= (abs (- (x1 l) (x2 l))) (abs (- (y1 l) (y2 l)))))
(define (diag-neg?) (and (diagonal? l) (> 0 (/ (- (y1 l) (y2 l)) (- (x1 l) (x2 l)))))) ; negative slope
(define (diag-pos?) (and (diagonal? l) (< 0 (/ (- (y1 l) (y2 l)) (- (x1 l) (x2 l)))))) ; positive slope

; read results into a list until eof
(define (read-all readfn f)
  (define (iter acc)
    (if (eof-object? (peek-char f))
      acc
      (iter (cons (readfn f) acc))))
  (iter '()))

(define (points-on-line l)
  (cond
    ((vertical? l) (map (lambda (y) (list (x1 l) y)) (range (y1 l) (y2 l))))
    ((horizontal? l) (map (lambda (x) (list x (y1 l))) (range (x1 l) (x2 l))))
    ((diagonal? l) (zip (range (x1 l) (x2 l)) (range (y1 l) (y2 l))))))

(define board-size 1000)

(define (board-row b n)
  (map (lambda (i)
         (vector-ref b (+ i (* board-size n))))
       (range 0 (dec board-size))))

(define (print-board b)
  (map (lambda (row)
         (print (board-row b row)))
       (range 0 (dec board-size))))

(define (solA lines)
  (define board (make-vector (square board-size) 0)) ; from (0,0) to (999, 999)
  (map (lambda (line)
         (map (lambda (point)
                (let ((idx (+ (x point) (* (y point) board-size))))
                  (vector-set! board idx (inc (vector-ref board idx)))))
              (points-on-line line)))
       lines)
  ; (print-board board)
  (print (vector-count (lambda (x) (< 1 x)) board)))

(define INFILE "day5.in")

; solA
(call-with-input-file INFILE
  (lambda (f)
    (define lines (filter (lambda (x) (or (horizontal? x) (vertical? x))) (read-all read-line-segment f)))
    (solA lines)))

; solB
; 22416 too high
(call-with-input-file INFILE
  (lambda (f)
    (define lines (read-all read-line-segment f))
    (solA lines)))
