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
type Point = (Int, Int)
type Segment = (Point, Point)

segments :: String -> [Segment]
segments input = [((0, 1), (2, 3))]

intersection :: Segment -> Segment -> Maybe Point
intersection x y = Nothing

manhattan :: Point -> Int
manhattan (x, y) = x + y

day3A :: String -> IO ()
day3A input = do
    let lines = splitOn "\n" input
    let wires1 = segments $ head lines
    let wires2 = segments $ last lines

    let intersections = catMaybes [intersection x y | x <- wires1, y <- wires2]
    let result = map manhattan intersections
    return ()

-- Main
main :: IO ()
main = do
    content <- getContents
    day2B content
