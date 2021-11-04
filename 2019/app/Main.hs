-- Advent of Code 2019

module Main where

import Debug.Trace
import Data.List.Split
import Data.Array
import Data.Maybe

-- Day 2
replaceChar :: Char -> Char -> String -> String
replaceChar x y = map (\c -> if c == x then y else c)

interpret :: Int -> Array Int Int -> Int
interpret ip code = do
    let arg1 = code ! (code ! (ip + 1))
    let arg2 = code ! (code ! (ip + 2))
    let res = code ! (ip + 3)
    let next = ip + 4
    -- print ip
    -- print code
    case code ! ip of
        1 -> interpret next (code // [(res, arg1 + arg2)])
        2 -> interpret next (code // [(res, arg1 * arg2)])
        99 -> code ! 0
        _ -> error "Invalid Instruction"

day2A :: String -> IO ()
day2A input = do
    let list = map read (words $ replaceChar ',' ' ' input)
    let code = listArray (0, length list - 1) list
    print (interpret 0 code)
    return ()

day2B :: String -> IO ()
day2B input = do
    let list = map read (words $ replaceChar ',' ' ' input)
    let code = listArray (0, length list - 1) list
    let a = [(x, y) | x <- [1..99], y <- [1..99], interpret 0 (code // [(1, x), (2, y)]) == 19690720]
    print a
    return ()

-- Day 3
{-# LANGUAGE MultiParamTypeClasses, TypeFamilies #-}
class Addable a b where
    type Result a
    (|+|) :: a -> b -> Result a b

data Point t = Point t t
    deriving (Eq, Show)
data Segment t = Segment (t Point) (t Point)
    deriving (Eq, Show)

instance Addable Point Point where
    type Result Point Point = Point
    (Point a b) |+| (Point c d) = Point (a + c) (b + d)

dot (Point x y) (Point p q) = x * y + p * q

from (Segment x _) = x
to (Segment _ y) = y

x (Point a _) = a
y (Point _ b) = b

segments :: String -> [t Segment]
segments input =
    let split = words $ replaceChar ',' ' ' input
        f :: [Segment] -> String -> [Segment]
        f (x:xs) (c:ch) =
            case c of
            'U' -> Segment (to x) (Point (x (to x)), second (second x) + read ch) : x : xs
            'R' -> Segment (to x) (first (second x) + read ch, second (second x)) : x : xs
            'D' -> Segment (to x) (first (second x), second (second x) - read ch) : x : xs
            'L' -> Segment (to x) (first (second x) - read ch, second (second x)) : x : xs
            _ -> error "invalid direction"
        f _ _ = error "invalid"
    in
    foldl f [((0, 0), (0, 0))] split


-- E = B-A = ( Bx-Ax, By-Ay )
-- F = D-C = ( Dx-Cx, Dy-Cy ) 
-- P = ( -Ey, Ex )
-- h = ( (A-C) * P ) / ( F * P )
-- if 0 < h < 1, intersection at C + F*h
intersection :: Num t => Segment t -> Segment t -> Maybe (Point t)
intersection (Segment a@(Point ax ay) b@(Point bx by)) (Segment c@(Point cx cy) d@(Point dx dy)) =
    let e = a - c
        f = (dx - cx, dy - cy)
        p = (- (y e), x e)
        fp = f `dot` p
        res = f `dot` p > (ax - cx, ay - cy) `dot` p
        h = ((ax - cx, ay - cy) `dot` p) / (f `dot` p)
    in
    if fp /= 0 && res then
        Just (cx + h * x f, cy + h * y f)
    else
        Nothing

manhattan :: Point t -> t
manhattan (Point x y) = x + y

day3A :: String -> IO ()
day3A input = do
    let lines = splitOn "\n" input
    let wires1 = segments $ head lines
    let wires2 = segments $ lines !! 1
    print wires1
    print wires2

    let intersections = catMaybes [intersection x y | x <- wires1, y <- wires2]
    print intersections
    let result = map manhattan intersections
    print result
    return ()

-- Main
main :: IO ()
main = do
    content <- getContents
    day3A content
