--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

parse :: [String] -> [[Int]]
parse s = map parseline s
    where
        parseline l     = map read $ filtered l
        filtered l      = filter (not . null) $ splitted l
        splitted l      = split ' ' $ (split ':' l)!!1

parse2 :: [String] -> (Int, Int)
parse2 s = (x, y)
    where [x, y] = map (read . filter (`elem` ['0'..'9'])) s

listToRaces :: [[Int]] -> [(Int, Int)]
listToRaces [x, y] = zip x y

-- Goal: Find number of ints solving the
-- equation x*(duration - x) > height
-- The interval containing the solutions
-- is
--      (duration/2)
--      +-
--      (1/2) sqrt(
--          duration - 4 * height
--      ).
-- The tricky/annoying part is counting
-- the integer points.

intsInParabolaCap:: (Int, Int) -> Int
intsInParabolaCap (duration, height)
    | even duration = evenResult
    | odd  duration = oddResult
    where
        evenResult
            | evenHitsEndpoints = 1 + 2*(integerHalfWidth-1)
            | otherwise         = 1 + 2*integerHalfWidth
        oddResult
            | even $ floor width  = integerWidth
            | odd  $ floor width  = 1 + integerWidth
        evenHitsEndpoints = fractionalHalfWidth == 0
        (integerHalfWidth, fractionalHalfWidth) = properFraction halfWidth
        (integerWidth, fractionalWidth) = properFraction width
        halfWidth   = 0.5 * width
        width       = sqrt (x^2 - 4*y)
        x           = fromIntegral duration
        y           = fromIntegral height

part1 :: [String] -> Int
part1 s = product gameResults
    where
        gameResults = map intsInParabolaCap games
        games = listToRaces $ parse s

part2 s = intsInParabolaCap $ parse2 s

main = do
    rawInput <- (readLines "06.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ listToRaces $ parse rawInput
    putStrLn $ show $ map intsInParabolaCap (listToRaces $ parse rawInput)
    putStrLn $ show $ part1 rawInput
    putStrLn $ show $ parse2 rawInput
    putStrLn $ show $ part2 rawInput
