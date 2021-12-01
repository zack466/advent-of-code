import Data.List

mapPairs :: (a -> a -> b) -> [a] -> [b]
mapPairs f [] = []
mapPairs f [x] = []
mapPairs f (x:y:zs) = f x y : (mapPairs f (y:zs))

repeatF :: Int -> (a -> a) -> a -> a
repeatF 0 f x = x
repeatF n f x = repeatF (n-1) f (f x)

-- takes each consecutive subsequence of length n
-- Ex: every 3 [1, 2, 3, 4, 5] = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
every :: Int -> [a] -> [[a]]
every n = dropLast (n-1) . transpose . take n . tails
    where
        dropLast n = repeatF n init
-- [[1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5]]

sol :: String -> Int
sol input = length $ filter (<0) $ mapPairs (-) $ map read $ words input

sol2 :: String -> Int
sol2 input = length $ filter (<0) $ mapPairs (\x -> \y -> (sum x) - (sum y)) $ every 3 $ map read $ words input

main = do
    input <- getContents
    print (sol2 input)
