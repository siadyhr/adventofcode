--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

parse :: [String] -> [[Int]]
parse ss = map parseLine ss
    where
        parseLine :: String -> [Int]
        parseLine s = map read (split ' ' s)

discreteDerivative :: [Int] -> [Int]
discreteDerivative [x, y] = [y-x]
discreteDerivative (x:xs) = (head xs - x):(discreteDerivative xs)

extrapolateNext :: [Int] -> Int
extrapolateNext xs
    | all (==0) xs  = 0
    | otherwise     = lastElement + (extrapolateNext dxs)
    where
        lastElement = head $ reverse xs 
        dxs         = discreteDerivative xs

extrapolatePrevious :: [Int] -> Int
extrapolatePrevious xs
    | all (==0) xs  = 0
    | otherwise     = firstElement - (extrapolatePrevious dxs)
    where
        firstElement    = head xs 
        dxs             = discreteDerivative xs

extrapolateNextList = map extrapolateNext
extrapolatePreviousList = map extrapolatePrevious

part1 :: [String] -> Int
part1 s = sum $ extrapolateNextList $ parse s

part2 :: [String] -> Int
part2 s = sum $ extrapolatePreviousList $ parse s

main = do
    rawInput <- (readLines "09.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ extrapolateNextList $ parse rawInput
    putStrLn $ show $ part1 rawInput
    putStrLn $ show $ extrapolatePreviousList $ parse rawInput
    putStrLn $ show $ part2 rawInput
