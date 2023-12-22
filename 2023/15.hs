--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Char (ord)
import MyAOCLib

parse :: String -> [[Int]]
parse rawInput = map (map ord) (split ',' rawInput)

hashStep :: Int -> Int -> Int
hashStep current new = ((current + new)*17) `mod` 256

hash :: [Int] -> Int
hash = foldl hashStep 0

part1 x = sum $ map hash (parse x)
part2 x = ""

part1OneLine :: String -> Int
part1OneLine x = sum $ map (foldl (\a b -> ((a + b :: Int)*17 `mod` 256)) 0) (map (map ord) (split ',' x))

main = do
    rawSampleInput <- (readLines "15sample.in")
    rawInput <- (readLines "15.in")

    putStrLn "Part 1"
    putStrLn $ show $ part1 $ head rawSampleInput
    putStrLn $ show $ part1 $ head rawInput
    putStrLn $ show $ part1OneLine $ head rawInput

    putStrLn "Part 2"
    putStrLn $ show $ part2 $ rawSampleInput
    putStrLn $ show $ part2 $ rawInput
